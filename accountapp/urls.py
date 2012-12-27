from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template
from registration.views import activate
from registration.views import register
from accountapp import settings

urlpatterns = patterns('',
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT}),
                       url(r'^activate/complete/$',
                           direct_to_template,
                           {'template': 'registration/activation_complete.html'},
                           name='registration_activation_complete'),

                       url(r'^accounts/activate/(?P<activation_key>\w+)/$',
                           activate,
                           {'backend': 'registration.backends.default.DefaultBackend'},
                           name='registration_activate'),
                       url(r'^register/$',
                           register,
                           {'backend': 'registration.backends.default.DefaultBackend'},
                           name='registration_register'),
                       url(r'^register/complete/$',
                           direct_to_template,
                           {'template': 'registration/registration_complete.html'},
                           name='registration_complete'),
                       url(r'^register/closed/$',
                           direct_to_template,
                           {'template': 'registration/registration_closed.html'},
                           name='registration_disallowed'),
                       url(r'^login/$', 'django.contrib.auth.views.login'),
                       url(r'^logout/$', 'account.views.logout_page'),
                       url(r'^$', 'django.contrib.auth.views.login'),
                       url(r'^loginsuccess/$', 'account.views.page'),
                       )

