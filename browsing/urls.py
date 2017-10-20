from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'inscriptions/$', views.InschriftListView.as_view(), name='browse_inscriptions'),
    url(r'map/$', views.MapView.as_view(), name='map'),
]
