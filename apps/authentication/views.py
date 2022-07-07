from django.http import HttpResponse
from django.shortcuts import render

from apps.authentication.models import User


def create_user(request):
    User.objects.create(username='123', password='123', is_admin=False)
    return HttpResponse('User Created')


def list_users(request):
    users = User.objects.all()
    return render(request, 'user-list.html', context={'users': users})


def my_view(request):
    return render(request, 'base.html')