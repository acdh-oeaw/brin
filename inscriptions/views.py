from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Inschrift
from .forms import InschriftForm


class InschriftDetailView(DetailView):
    model = Inschrift
    template_name = 'inscriptions/inschrift_detail.html'

    def get_context_data(self, **kwargs):
        context = super(InschriftDetailView, self).get_context_data(**kwargs)
        try:
            context["next_entry"] = Inschrift.objects.filter(id__gt=int(self.kwargs['pk']))[0].pk
        except:
            context["next_entry"] = None
        try:
            context["previous_entry"] = Inschrift.objects.filter(id__lt=int(self.kwargs['pk']))[0].pk
        except:
            context["previous_entry"] = None
        print(context['previous_entry'])
        return context


class InschriftListView(ListView):
    model = Inschrift
    template_name = 'inscriptions/inschrift_list.html'


class InschriftCreate(CreateView):

    model = Inschrift
    template_name = 'inscriptions/inschrift_create.html'
    form_class = InschriftForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InschriftCreate, self).dispatch(*args, **kwargs)


class InschriftUpdate(UpdateView):

    model = Inschrift
    template_name = 'inscriptions/inschrift_create.html'
    form_class = InschriftForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InschriftUpdate, self).dispatch(*args, **kwargs)
