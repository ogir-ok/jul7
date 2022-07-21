from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import get_user_model, login, logout
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from .forms import LoginForm, UserForm

User = get_user_model()


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'authentication/login.html'

    def form_valid(self, form):
        login(self.request, User.objects.get(email=form.cleaned_data['email']))
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', '/')


class RegisterView(FormView):
    form_class = UserForm
    success_url = '/'

    def form_valid(self, form):
        messages.add_message(self.request,
                             messages.SUCCESS,
                             'User successfully registered.'
                             ' We\'ve sent you an email to confirm your email address.')
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('accounts:user-login'))