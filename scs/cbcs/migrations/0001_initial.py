# Generated by Django 4.0.3 on 2022-04-08 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_roll', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50)),
                ('student_email', models.EmailField(max_length=50)),
                ('student_dept', models.CharField(max_length=5)),
            ],
        ),
    ]
