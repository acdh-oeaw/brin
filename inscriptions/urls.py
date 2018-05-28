from django.conf.urls import url
from . import views

app_name = 'inscriptions'

urlpatterns = [
    url(r'^$', views.InschriftListView.as_view(), name='inschrift_list'),
    url(r'^(?P<pk>[0-9]+)$', views.InschriftDetailView.as_view(), name='inschrift_detail'),
    url(r'^create/$', views.InschriftCreate.as_view(), name='inschrift_create'),
    url(r'^update/(?P<pk>[0-9]+)$', views.InschriftUpdate.as_view(), name='inschrift_update'),
]
