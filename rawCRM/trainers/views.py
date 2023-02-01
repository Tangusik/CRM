from django.shortcuts import render
from .models import Client


def index(request):
    client_list = Client.objects.order_by()
    context = {'client_list': client_list}
    return render(request, 'trainers/base.html', context)
