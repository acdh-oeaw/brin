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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InschriftDetailView, self).dispatch(*args, **kwargs)


class InschriftListView(ListView):
    model = Inschrift
    template_name = 'inscriptions/inschrift_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InschriftListView, self).dispatch(*args, **kwargs)


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
