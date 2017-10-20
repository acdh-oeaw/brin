from django_tables2 import SingleTableView, RequestConfig
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from inscriptions.models import *
from .filters import *
from .forms import *
from .tables import *


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    paginate_by = 25
    template_name = 'browsing/generic_list.html'

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        context['docstring'] = "{}".format(self.model.__doc__)
        if self.model.__name__.endswith('s'):
            context['class_name'] = "{}".format(self.model.__name__)
        else:
            context['class_name'] = "{}s".format(self.model.__name__)
        return context


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
    #init_columns = ['legacy_id', 'gattung', 'traeger', 'resch_kopial_signatur']

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
