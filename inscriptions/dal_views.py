from dal import autocomplete
from .models import Person
from django.db.models import Q
from vocabs.models import SkosConceptScheme


class PersonAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
