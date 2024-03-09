from django.http import HttpResponse

from django.shortcuts import render
import json
from .models import Todo


# Create your views here.

def todo_check(request):
    todo = Todo.objects.get(pk=request.POST.get('todo_id'))
    todo.completed = not todo.completed
    todo.save()
    return HttpResponse(json.dumps({'status': 'success'}))

