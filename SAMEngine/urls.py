from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SAMEngine.views.home', name='home'),
    # url(r'^SAMEngine/', include('SAMEngine.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^same/admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^same/admin/', include(admin.site.urls)),

    url(r'^same/character/', include('characters.urls')),
    url(r'^same/battle/', include('battles.urls')),
    url(r'^same/ui/', include('visuals.urls')),
)
