from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^login/$',auth_views.login, name='login'),
    url('^logout/$', auth_views.logout, name='logout'),
]