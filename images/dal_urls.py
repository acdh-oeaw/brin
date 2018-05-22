from django.conf.urls import url
from . import views
from . import dal_views
from . models import Image

urlpatterns = [
    url(
        r'^image/$', dal_views.ImageAC.as_view(model=Image),
        name='image-autocomplete',
    ),
]
