from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<article_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<article_id>[0-9]+)/content$', views.content, name='content'),
]
