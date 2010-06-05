#-*- coding: UTF-8 -*-
from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __unicode__(self):
        return '%s' % self.question


class Lol(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    loltext = models.TextField()

    def __unicode__(self):
        return '%s - %s' % (self.id, self.text[:15])

    @models.permalink
    def get_absolute_url(self):
        return ('share_lol', [str(self.id)])
