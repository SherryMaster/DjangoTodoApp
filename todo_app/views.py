from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo


# Create your views here.
class IndexView(ListView):
    model = Todo
    template_name = 'todo_app/index.html'


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_app/todo_detail.html'


class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'description', 'completed']
    template_name = 'todo_app/todo_create.html'
    success_url = reverse_lazy('todo_app:home')
