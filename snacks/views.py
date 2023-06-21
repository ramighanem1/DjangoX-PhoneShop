from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy


# Create your views here.

class SnackListView(ListView):
    template_name="snacks/snack_list.html"
    model=Snack
    context_object_name = "Snacks"


class SnackDetailsView(DetailView):
    template_name="snacks/snack_detail.html"
    model=Snack

class SnackCreateView(CreateView):
    model = Snack
    template_name = 'snacks/snack_create.html'
    fields = ['name', 'purchaser', 'description']


class SnackUpdateView(UpdateView):
    template_name='snacks/snack_update.html'
    model=Snack
    fields="__all__"
    success_url=reverse_lazy('snacks')

class SnackDeleteView(DeleteView):
    template_name='snacks/snack_delete.html'
    model=Snack
    success_url=reverse_lazy('snacks')
