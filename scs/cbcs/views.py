from django.shortcuts import render


def student(request):
    return render(request, 'profile.html')


def course(request):
    return render(request, 'base.html')
