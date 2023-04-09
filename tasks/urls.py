from django.urls import path
from .views import *

urlpatterns = [
    path('task/<int:task_id>', view_task, name='task'),
    path('all_tasks/', all_tasks, name='all_tasks')
]