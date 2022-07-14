from django.urls import path

from .views import login_view, logout_view

app_name = 'apps.authentication'

urlpatterns = [
    path('login/', login_view, name='user-login'),
    path('logout/', logout_view, name='user-logout')
]