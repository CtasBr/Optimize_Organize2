from django.contrib.auth import login, logout
from django.contrib.auth import models
from django.shortcuts import render, redirect

from .forms import *


def register(request):
    if request.method == 'POST':
        print(1)
        email = request.POST.get('email')
        pas = request.POST.get('ps')
        pas1 = request.POST.get('ps1')
        username = request.POST.get('username')
        name = request.POST.get('name')
        job_title = request.POST.get('job_title')
        user = models.User.objects.create(username=username, password=pas, email=email)
        s_name = request.POST.get('s_name')
        p_series = request.POST.get('p_series')
        p_number = request.POST.get('p_number')
        org = request.POST.get('org')
        profile = Profile.objects.create(user=user, s_name=s_name, name=name, p_series=p_series, job_title=job_title,
                                         p_number=p_number, org=org)
        user.save()
        profile.save()
        return redirect('login')
    else:
        register_form = UserRegisterForm()
        profile_form = ProfileForm()
        data = {
            'form': register_form,
            'form1': profile_form,
        }
        return render(request, 'users/register.html', data)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            print(1)
            user = form.get_user()
            login(request, user)
            return redirect('dashboard', 'objects')
    else:
        form = UserLoginForm()
        data = {
            'form': form,
        }
        return render(request, 'users/login.html', data)


def user_logout(request):
    logout(request)
    return redirect('login')
