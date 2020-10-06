from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Todo

class IndexView(generic.ListView):
    model = Todo
    paginate_by = 5
