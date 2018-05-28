from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Inschrift, Person
from .forms import InschriftForm, PersonForm
from images.models import Image


class PersonDetailView(DetailView):
    model = Person
    template_name = 'inscriptions/person_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonDetailView, self).dispatch(*args, **kwargs)


class PersonListView(ListView):
    model = Person
    template_name = 'inscriptions/person_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonListView, self).dispatch(*args, **kwargs)


class PersonCreate(CreateView):

    model = Person
    template_name = 'inscriptions/person_create.html'
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonCreate, self).dispatch(*args, **kwargs)


class PersonUpdate(UpdateView):

    model = Person
    template_name = 'inscriptions/person_create.html'
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonUpdate, self).dispatch(*args, **kwargs)


class InschriftDetailView(DetailView):
    model = Inschrift
    template_name = 'inscriptions/inschrift_detail.html'

    def get_context_data(self, **kwargs):
        context = super(InschriftDetailView, self).get_context_data(**kwargs)
        to_remove = self.request.GET.getlist('to_remove')
        if to_remove and self.request.user.is_authenticated():
            context['to_remove'] = to_remove
            images = Image.objects.filter(id__in=to_remove)
            inscript = self.get_object()
            for x in images:
                inscript.images.remove(x)
        else:
            context['to_remove'] = None
        return context

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
