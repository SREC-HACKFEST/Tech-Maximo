from django.db import models

# Create your models here.


class Student(models.Model):
    student_roll = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=50)
    student_dept = models.CharField(max_length=5)

    def __str__(self):
        return self.student_name


class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=50)
    teacher_email = models.EmailField(max_length=50)

    def __str__(self):
        return self.teacher_name


class Course(models.Model):
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=70)
    course_staff = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.course_name
