import datetime
import random

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from tasks.models import *
from .models import *

b = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque a lectus at metus aliquet consequat. Nunc leo purus, feugiat eu ante vitae, vehicula gravida turpis. Aenean eget interdum turpis. Nullam pharetra interdum dui. Proin magna arcu, fermentum at convallis non, elementum sed est. Phasellus et metus arcu. Curabitur mollis molestie imperdiet. In nec est ut tortor gravida interdum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Ut nec sagittis nunc. Nulla vitae mauris massa. Duis tristique leo id odio rhoncus laoreet. Mauris non est id quam iaculis volutpat nec nec magna. Proin in erat sed felis placerat dapibus quis eget nulla. Aenean quis nunc orci.'
b = b.split()


def uppender(request):
    for i in range(19):
        obj = ObjectTable(

            address=b[random.randint(0, len(b) - 1)]
            , administrate_county=b[random.randint(0, len(b) - 1)]
            , cod_number=b[random.randint(0, len(b) - 1)]
            , ind_zone=True
            , date=b[random.randint(0, len(b) - 1)]
            , area=b[random.randint(0, len(b) - 1)]
            , comments=b[random.randint(0, len(b) - 1)]
            , rev_count=11
            , type_obj=b[random.randint(0, len(b) - 1)]
            , state_obj=b[random.randint(0, len(b) - 1)]
            , sqr=152
            , own=b[random.randint(0, len(b) - 1)]
            , actual_user=b[random.randint(0, len(b) - 1)]
            , n_prot=b[random.randint(0, len(b) - 1)]
            , city=b[random.randint(0, len(b) - 1)]
            , check_company=b[random.randint(0, len(b) - 1)]
            , law='ПП-17')
        obj.save()
    return redirect('dashboard', 'objects')

def index(request):
    return redirect('dashboard', 'objects')


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
