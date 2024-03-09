from django.urls import path
from . import views
from . import apis

app_name = 'todo_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('todo/<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('todo/create/', views.TodoCreateView.as_view(), name='todo_create'),

    # APIs
    path('todo/check/', apis.todo_check, name='todo_check'),
]