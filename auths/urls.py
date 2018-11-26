from django.conf.urls import url
from .views import register, user_login, user_logout, user_profile, user_settings, user_about, user_password_change

urlpatterns = [
    url(r'^register/$', view=register, name='register'),
    url(r'^login/$', view=user_login, name='user-login'),
    url(r'^logout/$', view=user_logout, name='user-logout'),
    url(r'^settings/$', view=user_settings, name='user-settings'),
    url(r'^password-change/$', user_password_change, name='user-password-change'),
    url(r'^(?P<username>[-\w]+)/$', view=user_profile, name='user-profile'),
    url(r'^(?P<username>[-\w]+)/about/$', view=user_about, name='user-about')
]
