from django.urls import path

from .views import list_students

app_name = 'apps.lms'

urlpatterns = [
    path('', list_students, name='list-students')
]