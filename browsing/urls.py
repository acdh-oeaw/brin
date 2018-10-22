from django.conf.urls import url
from . import views

app_name = 'browsing'

urlpatterns = [
    url(r'inscriptions/$', views.InschriftListView.as_view(), name='browse_inscriptions'),
    url(r'persons/$', views.PersonListView.as_view(), name='browse_persons'),
    url(r'map/$', views.MapView.as_view(), name='map'),
    url(r'references/$', views.ReferenceListView.as_view(), name='browse_references'),
]
