import django_filters
from dal import autocomplete
from inscriptions.models import Inschrift
from vocabs.models import SkosConcept

django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class InschriftListFilter(django_filters.FilterSet):
    transkription = django_filters.CharFilter(
        lookup_expr='icontains',
        label="Transkription"
        )
    transkription_normalized = django_filters.CharFilter(
        lookup_expr='icontains',
        label="Transkription normalized"
        )
    resch_kopial_signatur = django_filters.CharFilter(
        lookup_expr='icontains',
        label="Resch kopial signatur"
        )

    class Meta:
        model = Inschrift
        fields = '__all__'
