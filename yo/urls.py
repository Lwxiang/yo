from django.conf.urls import patterns, include, url
from share.views import *
from organize.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^index/', index),
    ('^login/', Login),
    ('^logout/', Logout),
    ('^register/$', register_page),
    ('^register/send/$', register),
    ('^share/edit/$', edit_share),
    ('^share/list/(.+)/$', share_list),
    ('^share/$', share),
    ('^share/(.+)/(\d{4})/$', share_page),
    ('^share/comment/$', make_comment_share),
    ('^date/edit/$', edit_organize),
    ('^date/list/(.+)/$', organize_list),
    ('^date/$', organize),
    ('^date/(.+)/(\d{4})/$', organize_page),
    ('^date/comment/$', make_comment_date),
    ('^join/$', join_date),
    # Examples:
    # url(r'^$', 'yo.views.home', name='home'),
    # url(r'^yo/', include('yo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
