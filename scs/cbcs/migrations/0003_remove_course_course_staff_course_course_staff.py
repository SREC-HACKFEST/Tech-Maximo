# Generated by Django 4.0.3 on 2022-04-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbcs', '0002_teacher_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_staff',
        ),
        migrations.AddField(
            model_name='course',
            name='course_staff',
            field=models.ManyToManyField(to='cbcs.teacher'),
        ),
    ]