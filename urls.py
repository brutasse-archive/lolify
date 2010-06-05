from django.conf.urls.defaults import *
from django.conf import settings
from django.http import HttpResponse

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^', include('lol.urls')),
    (r'^admin/', include(admin.site.urls)),

    url(r'^robots.txt$',
        lambda _: HttpResponse('User-agent: *\nDisallow:\n',
                               mimetype='text/plain')),
    url(r'^favicon.ico$', lambda _: HttpResponse('')),
)


if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        url(r'^static/(?P<path>.*)$', 'serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
