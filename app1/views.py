from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import AddActivity

class AddCreateView(CreateView):
    model = AddActivity
    fields = "__all__"
    success_url = '/view/'

class viewListView(ListView):
    model = AddActivity
    context_object_name = 'activities'

class DeleteactivityDeleteView(DeleteView):
    model = AddActivity
    success_url = '/view/'

class UpdateActivityUpdateView(UpdateView):
    model = AddActivity
    fields="__all__"
    success_url = '/view/'