from django.urls import path

from .views import ListStudentsView

app_name = 'apps.lms'

urlpatterns = [
    path('', ListStudentsView.as_view(), name='list-students')
]