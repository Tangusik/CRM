from django.shortcuts import render
from .models import Client
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    client_list = Client.objects.order_by()

    if request.user.is_authenticated:
        context = {'client_list': client_list, 'userinfo': request.user}
    else:
        context = {'client_list': client_list}

    return render(request, 'trainers/base.html', context)


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return HttpResponseRedirect(reverse('index'))


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
