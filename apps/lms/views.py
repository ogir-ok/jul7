from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, FormView

from apps.lms.forms import GroupForm
from apps.lms.models import Student, Group, Teacher


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