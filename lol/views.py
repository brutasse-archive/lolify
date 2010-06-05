#-*- coding: UTF-8 -*-
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic.simple import direct_to_template

from lol.forms import LolForm
from lol.models import Lol


'''Quotes are supposed to be testimonials from happy(c) proud(r) users.'''
QUOTES = (
        (u'Lol sa sé du lour', u'Abd Al Malik'),
        (u'Jé toujour révé douvriR 1 skyblog lol', u'1 skyblogueur anonim'),
        (u'Kikoo', u'Brutasse, kréateur 2 Lolify'),
        (u'Grass a Lolify jpeu parlé kikoo lol', u'1 kikoo-lol eureu'),
        (u'Aven jcomprené pa mé pot dé skyblog é m1tenan jparl mieu keu mdr', u'turc-du-83'),
        (u'Lol il doi assuré le ga ki a fé sa pr répertorié ts lé mo', u'Anne onime'),
        (u'Lol tro le kiff mdr lol', u'Esmeralda'),
    )


def home(request):
    '''Basically display a LolForm to let the user type the text
    to translate'''
    form = LolForm()
    context = {'form': form}
    return render_to_response('home.html', context,
                              context_instance=RequestContext(request))


def lolify(request):
    '''Checks the `lol` parameter exists and renders the lol-translated text'''
    if not request.method == 'POST' or not request.POST['lol']:
        return redirect(reverse('home'))

    lol = request.POST['lol']
    context = {'lol': lol}
    return render_to_response('home.html', context,
                              context_instance=RequestContext(request))


def question(request):
    '''Send the question to the manager'''
    if request.method == 'POST' and request.POST['q']:
        mail_admins(u'Question ^^', u'%s\n\n%s' % (request.POST['q'], request))
        return direct_to_template(request, 'sent.html')
    else:
        return redirect(reverse('fok'))


def share(request):
    if request.method == 'POST' and request.POST['action'] == 'share':
        text = request.POST['text']
        loltext = request.POST['loltext']
        lol = Lol(text=text, loltext=loltext)
        lol.save()
        return render_to_response('share.html', locals(),
                                  context_instance=RequestContext(request))
    else:
        return redirect(reverse('home'))
