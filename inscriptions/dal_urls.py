from django.conf.urls import url
from . import views
from . import dal_views
from . models import Person

app_name = 'inscriptions'

urlpatterns = [
    url(
        r'^person-autocomplete/$', dal_views.PersonAC.as_view(
            model=Person, create_field='name',),
        name='person-ac',
    ),
]
