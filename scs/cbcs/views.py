from django.shortcuts import render
from .models import Course, Teacher


def student(request):
    return render(request, 'profile.html')


def course(request):
    courses = Course.objects.all()
    teacher = Teacher.objects.all()
    return render(request, 'course.html', {"courses": courses, "teacher": teacher, "tc": [i for i in range(1, teacher.count()+1)]})


def csel(request):
    return render(request, 'base.html')
