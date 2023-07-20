from typing import Any, Dict
from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import student 

class MyModelListView(ListView):
    model = student
    template_name = 'list.html'
    paginate_by=10
    

class MyModelCreateView(CreateView):
    model = student 
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('CRUD:home')

class MyModelUpdateView(UpdateView):
    model = student
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('CRUD:home')

class MyModelDeleteView(DeleteView):
    model = student
    template_name = 'delete.html'
    success_url = reverse_lazy('CRUD:home')


def home(request):
    return render(request,'home.html')
