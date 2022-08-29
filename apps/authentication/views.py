from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import get_user_model, login, logout
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, CreateView
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import LoginForm, UserForm
from .tasks import send_invitation_email

User = get_user_model()


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'authentication/login.html'

    def form_valid(self, form):
        login(self.request, User.objects.get(email=form.cleaned_data['email']))
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', '/')


class RegisterView(CreateView):
    form_class = UserForm
    success_url = '/'
    template_name = 'authentication/register.html'

    def send_confirmation_email(self):
        send_invitation_email.delay(self.object.id)

    def form_valid(self, form):
        res = super().form_valid(form)
        self.send_confirmation_email()
        messages.add_message(self.request,
                             messages.SUCCESS,
                             'User successfully registered.'
                             ' We\'ve sent you an email to confirm your email address.')
        return res


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('accounts:user-login'))


class CurrentUserAPIView(APIView):
    def get(self, request):
        return Response({'user': str(request.user)})