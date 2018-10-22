from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Inschrift, Person, Reference
from .forms import InschriftForm, PersonForm, ReferenceForm
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


class PersonDelete(DeleteView):
    model = Person
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_persons')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonDelete, self).dispatch(*args, **kwargs)


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


class InschriftDelete(DeleteView):
    model = Inschrift
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_inscriptions')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InschriftDelete, self).dispatch(*args, **kwargs)


class ReferenceDetailView(DetailView):
    model = Reference
    template_name = 'inscriptions/reference_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReferenceDetailView, self).dispatch(*args, **kwargs)


class ReferenceListView(ListView):
    model = Reference
    template_name = 'inscriptions/reference_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReferenceListView, self).dispatch(*args, **kwargs)


class ReferenceCreate(CreateView):

    model = Reference
    template_name = 'inscriptions/reference_create.html'
    form_class = ReferenceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReferenceCreate, self).dispatch(*args, **kwargs)


class ReferenceUpdate(UpdateView):

    model = Reference
    template_name = 'inscriptions/reference_create.html'
    form_class = ReferenceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReferenceUpdate, self).dispatch(*args, **kwargs)


class ReferenceDelete(DeleteView):
    model = Reference
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_persons')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReferenceDelete, self).dispatch(*args, **kwargs)
