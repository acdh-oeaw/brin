from django_tables2 import SingleTableView, RequestConfig
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from inscriptions.models import *
from . filters import *
from . forms import *
from . tables import *
from . browsing_utils import GenericListView, BaseCreateView, BaseUpdateView


class ReferenceListView(GenericListView):
    model = Reference
    table_class = ReferenceTable
    filter_class = ReferenceListFilter
    formhelper_class = ReferenceFilterFormHelper
    init_columns = ['id', 'short_title']

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(ReferenceListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


class PersonListView(GenericListView):
    model = Person
    table_class = PersonTable
    filter_class = PersonListFilter
    formhelper_class = PersonFilterFormHelper
    init_columns = ['id', 'name', 'titel_grad_beruf']

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


class InschriftListView(GenericListView):
    model = Inschrift
    table_class = InschriftTable
    filter_class = InschriftListFilter
    formhelper_class = InschriftFilterFormHelper
    init_columns = ['legacy_id', 'gattung', 'traeger', 'resch_kopial_signatur']

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(InschriftListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


class MapView(GenericListView):
    model = Inschrift
    table_class = InschriftTable
    filter_class = InschriftListFilter
    formhelper_class = InschriftFilterFormHelper
    template_name = 'browsing/map_view.html'
    # init_columns = ['legacy_id', 'gattung', 'traeger', 'resch_kopial_signatur']

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        inschrifts = []
        for x in self.get_queryset():
            inschrifts.append(x)
        context["inschrifts"] = set(inschrifts)
        # togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        # context['togglable_colums'] = togglable_colums
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MapView, self).dispatch(*args, **kwargs)
