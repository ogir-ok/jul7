from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView

from apps.lms.models import Student, Group


class ListStudentsView(LoginRequiredMixin, CreateView):
    template_name = 'lms/students-list.html'
    model = Student
    fields = ['name', 'birth_date']