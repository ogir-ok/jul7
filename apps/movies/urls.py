from django.urls import path

from .views import movies_list

app_name = 'apps.movies'

urlpatterns = [
    path('', movies_list, name='movies-list')
]