from django.urls import path

from .views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView

app_name = 'apps.lms'

urlpatterns = [
    path('student/', StudentListCreateAPIView.as_view(), name='sudent-list-create'),
    path('student/<str:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='sudent-list-create'),
]

