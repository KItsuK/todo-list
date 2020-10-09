from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import TodoForm
from .models import Todo

class IndexView(generic.ListView):
    model = Todo
    paginate_by = 5

class DetailView(generic.DetailView):
    model = Todo

class CreateView(generic.CreateView):
    model = Todo
    success_url = reverse_lazy('todo:index')
    form_class = TodoForm

class UpdateView(generic.UpdateView):
    model = Todo
    success_url = reverse_lazy('todo:index')
    form_class = TodoForm

class DeleteView(generic.DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:index')
