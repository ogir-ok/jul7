from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import get_user_model, login, logout
from django.urls import reverse

User = get_user_model()


def login_view(request):
    if request.method == 'GET':
        return render(request, 'authentication/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(email=username).first()
        if user and user.check_password(password):
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', '/'))
        else:
            return render(request, 'authentication/login.html', context={'error': 'Error occured', 'username': request.POST['username']})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:user-login'))