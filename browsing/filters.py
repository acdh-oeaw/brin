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
        help_text=Inschrift._meta.get_field('transkription').help_text,
        label=Inschrift._meta.get_field('transkription').verbose_name
        )
    transkription_normalized = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Inschrift._meta.get_field('transkription_normalized').help_text,
        label=Inschrift._meta.get_field('transkription_normalized').verbose_name
        )
    resch_kopial_signatur = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Inschrift._meta.get_field('resch_kopial_signatur').help_text,
        label=Inschrift._meta.get_field('resch_kopial_signatur').verbose_name
        )

    class Meta:
        model = Inschrift
        fields = '__all__'
