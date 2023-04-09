from django.shortcuts import render, get_object_or_404

from .models import *


def view_task(request, task_id):
    task = get_object_or_404(TaskTable, id=task_id)
    data = {
        'task': task,
    }
    return render(request, 'tasks/task.html', data)


def all_tasks(request):
    tasks = TaskTable.objects.order_by('date').filter(done=False)
    data = {
        'tasks': tasks,
    }
    return render(request, 'tasks/all_tasks.html', data)
