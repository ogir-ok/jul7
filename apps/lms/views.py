from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, FormView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.lms.forms import GroupForm
from apps.lms.models import Student, Group, Teacher
from apps.lms.serializers import StudentSerializer, StudentSerializerMin


class CreateStudentView(LoginRequiredMixin, CreateView):
    template_name = 'lms/students-list.html'
    model = Student
    fields = ['name', 'birth_date']


class ListStudentsView(ListView):
    template_name = 'lms/students-list.html'
    model = Teacher


class SecondPageView(FormView):
    template_name = 'lms/second-page.html'
    form_class = GroupForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['teachers_list'] = self.request.GET.getlist('students')
        return kwargs


class StudentListCreateAPIView(ListCreateAPIView):
    serializer_class = StudentSerializerMin

    def get_queryset(self):
        return Student.objects.all()

class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()

