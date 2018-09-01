from django.conf.urls import url
from . import views

app_name = 'inscriptions'

urlpatterns = [
    url(r'^$', views.InschriftListView.as_view(), name='inschrift_list'),
    url(r'^(?P<pk>[0-9]+)$', views.InschriftDetailView.as_view(), name='inschrift_detail'),
    url(r'^create/$', views.InschriftCreate.as_view(), name='inschrift_create'),
    url(r'^update/(?P<pk>[0-9]+)$', views.InschriftUpdate.as_view(), name='inschrift_update'),
    url(r'^persons/$', views.PersonListView.as_view(), name='person_list'),
    url(r'^person/(?P<pk>[0-9]+)$', views.PersonDetailView.as_view(), name='person_detail'),
    url(r'^person/create/$', views.PersonCreate.as_view(), name='person_create'),
    url(r'^person/update/(?P<pk>[0-9]+)$', views.PersonUpdate.as_view(), name='person_update'),
    url(r'^person/delete/(?P<pk>[0-9]+)$', views.PersonDelete.as_view(),
        name='person_delete'),
]
