from django.conf.urls import patterns, include, url
from MemeShare.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

      ('^hello/$', hello),
      ('^test/$', test),
      ('^testadd/$', add_memegroup),
      ('^testadduser/$', add_user),
      ('^get/$', test_get_user_memegroups),
    # Examples:
    # url(r'^$', 'MemeShare.views.home', name='home'),
    # url(r'^MemeShare/', include('MemeShare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
