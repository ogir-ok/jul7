from django.urls import path

from .views import my_view, create_user, list_users

app_name = 'apps.authentication'

urlpatterns = [
    path('', my_view),
    path('create-user/', create_user),
    path('list-users/', list_users),
    path('my-view/', my_view),
]