import django_tables2 as tables
from django_tables2.utils import A
from inscriptions.models import *


class InschriftTable(tables.Table):
    legacy_id = tables.LinkColumn(
        'inschriften:inschrift_detail',
        args=[A('pk')], verbose_name='ID'
    )
    gattung = tables.TemplateColumn(template_name='browsing/tables/gattung.html')

    class Meta:
        model = Inschrift
        sequence = ('legacy_id', 'gattung', 'resch_kopial_signatur')
        attrs = {"class": "table table-responsive table-hover"}