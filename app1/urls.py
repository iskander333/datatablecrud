
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addnew$', views.addnew),
    url(r'^edit/(?P<id>\d+)/$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.destroy),
]
