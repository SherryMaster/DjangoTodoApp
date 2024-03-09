from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'todo_app/index.html'
