from django.conf.urls.defaults import *

from lol.models import Faq, Lol
from lol.forms import FaqForm

info_dict = {
        'queryset': Faq.objects.all(),
        'template_name': 'faq.html',
        'extra_context': {'form': FaqForm()},
}

lol_dict = {
        'queryset': Lol.objects.all(),
        'template_name': 'lol.html',
}

urlpatterns = patterns('lol.views',
    url(r'^$', 'home', name='home'),
    url(r'^lol/share/$', 'share', name='share'),
    url(r'^lol/$', 'lolify', name='lol'),
    url(r'^fok/ask/$', 'question', name='question'),
)

urlpatterns += patterns('django.views.generic.list_detail',
    url(r'^lol/(?P<object_id>\d+)$', 'object_detail',
        lol_dict, name='share_lol'),

    url(r'^fok/$', 'object_list', info_dict, name='fok'),
)
