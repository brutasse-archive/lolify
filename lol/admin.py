#-*- coding: UTF-8 -*-
from django.contrib import admin

from lol.models import Faq, Lol


class FaqAdmin(admin.ModelAdmin):

    class Meta:
        model = Faq


class LolAdmin(admin.ModelAdmin):

    class Meta:
        model = Lol


admin.site.register(Faq, FaqAdmin)
admin.site.register(Lol, LolAdmin)
