import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from tasks.models import *
from .models import *


def dashboard(request, item='objects'):
    if item == 'objects':
        a_cards = ObjectTable.objects.order_by('date')
        cards = []
        y = 0

        for i in a_cards:
            time_now = datetime.date.today()
            if int((time_now - i.date).days) < 5:
                b = [i, 'card-date-red']
            elif 5 <= int((time_now - i.date).days) < 10:
                b = [i, 'card-date-yellow']
            elif 10 <= int((time_now - i.date).days) < 20:
                b = [i, 'card-date-orange']
            else:
                b = [i, 'card-date-green']
            cards.append(i)
            y += 1
            if y == 6:
                break
        data = {
            'cards': cards
        }
        return render(request, 'objects/objects.html', data)
    elif item == 'tasks':
        all_tasks = TaskTable.objects.order_by('date').filter(done=False)
        y = 0
        tasks = []
        for i in all_tasks:
            tasks.append(i)
            y += 1
            if y == 5:
                break
        data = {
            'tasks': tasks
        }
        return render(request, 'objects/tasks.html', data)
    elif item == 'stats':
        data = {

        }
        return render(request, 'objects/stats.html', data)


def registry(request):
    obj = ObjectTable.objects.all()
    paginator = Paginator(obj, 9)
    try:
        page_number = request.GET.get('page')
    except:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    data = {
        'obj': obj,
        'page_obj': page_obj,
    }
    return render(request, 'objects/registry.html', data)


def view_object(request, object_id):
    obj = get_object_or_404(ObjectTable, id=object_id)
    data = {
        'obj': obj,
    }
    return render(request, 'objects/object.html', data)
