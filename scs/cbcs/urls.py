from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.student, name="student"),
    path('courses/', views.course, name="course")
]
