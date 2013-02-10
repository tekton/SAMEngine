from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import login, logout_then_login  # , register  # , password_change

urlpatterns = patterns('',
    url(r'register', 'auth.views.RegistrationPage'),
    url(r'login', login, {"redirect_field_name": "next"}),
    url(r'logout', logout_then_login),
)
