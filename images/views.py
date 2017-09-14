from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Image


class ImageDetailView(DetailView):
    model = Image
    template_name = 'images/image_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ImageDetailView, self).dispatch(*args, **kwargs)


class ImageListView(ListView):
    model = Image
    template_name = 'images/image_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ImageListView, self).dispatch(*args, **kwargs)
