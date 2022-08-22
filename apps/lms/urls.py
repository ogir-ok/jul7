from django.urls import path

from .views import ListStudentsView, SecondPageView

app_name = 'apps.lms'

urlpatterns = [
    path('', ListStudentsView.as_view(), name='list-students'),
    path('second-page', SecondPageView.as_view(), name='second-page'),
]

