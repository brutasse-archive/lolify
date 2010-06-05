#-*- coding: UTF-8 -*-
from django import template

import re

from random import choice

from lol.views import QUOTES

register = template.Library()


class RandomQuoteNode(template.Node):

    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = choice(QUOTES)
        return ''


@register.tag
def get_random_quote(parser, token):
    '''Usage: {% get_random_quote as quote %}

    Then display your quote using {{ quote.0 }} for quote content and
    {{ quote.1 }} for the author.'''
    bits = token.contents.split()
    if len(bits) != 3:
        raise template.TemplateSyntaxError("get_random_quote takes exactly "
                                           "two arguments")
    if bits[1] != 'as':
        raise template.TemplateSyntaxError("first argument to get_random_quote"
                                           "tag must be 'as'")
    return RandomQuoteNode(bits[2])


@register.filter
def lol(value):
    '''Usage: {{ my_string|lol }}

    Displays the converted string. See `process_lol` below.'''
    return process_lol(value)


def punctuation():
    words = (
            'lol',
            'XD',
            'mdr',
        )
    return ' %s' % choice(words)


def process_lol(mylol):
    patterns = (
            # (regexp, substitute),
            (re.compile(u' (j\'ai) ', re.I), u' G '),
            (re.compile(r'in([^aeiouyéèà])', re.I), r'1\1'),
            (re.compile(r'c([ltr])', re.I), r'k\1'),
            (re.compile(r' ([bB])onjour ', re.I), r' \1jr '),
            (re.compile(u' [cC][ \']est ', re.I), u' sé '),
        )
    words = (
            (u'ain', u'1'),
            (u' quand ', u' kan '),
            (u' soit ', u' soi '),
            (u' coucou ', u' kikoo '),
            (u' vacances ', u' vacs '),
            (u' trop ', u' tro '),
            (u' d\'abord ', u' dabor '),
            (u' ses ', u' sé '),
            (u' ce ', u' se '),
            (u' est ', u' è '),
            (u' cela ', u' sela '),
            (u'ais ', u'é '),
            #(u'ai', u'é'),
            (u' je ne ', u' j'),
            (u'ça', u'sa'),
            (u'ç', u'ss'),
            (u'ge ', u'j '),
            (u'ien', u'i1'),
            (u' qu\'eux', u' keu '),
            (u'qu\'', u'k'),
            (u'qu', u'k'),
            (u' des ', u' dé '),
            (u' mes ', u' mé '),
            (u'je me ', u'jme '),
            (u'hier ', u'iR '),
            (u'té ', u'T '),
            (u' h', u' '),
            (u'dit ', u'di '),
            (u'ff', u'f'),
            (u'mm', u'm'),
            (u'nn', u'n'),
            (u' et ', u' é '),
            (u' les ', u' lé '),
            (u' dès ', u' dè '),
            (u' pas ', u' pas '),
            (u' de ', u' 2 '),
            (u' un ', u' 1 '),
            (u' ben ', u' bin '),
            (u'use ', u'uz '),
            (u'eux ', u'eu '),
            (u'tés ', u'T '),
            (u'tes ', u'T '),
            (u'té ', u'T '),
            (u'ez ', u'é '),
            (u'ns ', u'n '),
            (u'ées ', u'é '),
            (u'ée ', u'é '),
            (u'elles ', u'L '),
            (u'elle ', u'L '),
            (u'er ', u'é '),
            (u'ssés ', u'C '),
            (u'ssé ', u'C '),
            (u'es ', u'e '),
            (u'is ', u'i '),
            (u'ait ', u'é '),
            (u'nné ', u'né '),
            (u'aire ', u'ère '),
            (u'l\'h', u'l'),
            (u'l\'a', u'la'),
            (u'd\'é', u'dé'),
            (u'l\'é', u'lé'),
            (u's\'a', u'sa'),
            (u' n\'y ', u' ni '),
            (u'cc', u'k'),
            (u' ca', u' ka'),
            (u'th', u't'),
            (u' con', u' kon'),
            (u'isé ', u'izé '),
            (u' cette ', u' sette '),
            (u' tech', u' tek'),
        )
    mylol = " %s " % mylol
    while re.search(r'[\.,?!]', mylol):
        mylol = mylol.replace('.', punctuation(), 1)
        mylol = mylol.replace(',', punctuation(), 1)
        mylol = mylol.replace('?', punctuation(), 1)
        mylol = mylol.replace('!', punctuation(), 1)
    for word in words:
        mylol = mylol.replace(word[0], word[1])
    for pattern in patterns:
        mylol = pattern[0].sub(pattern[1], mylol)
    return "Lol %s" % mylol
