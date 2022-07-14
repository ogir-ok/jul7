from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def list_students(request):
    return render(request, 'lms/students-list.html')