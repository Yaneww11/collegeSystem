# Generated by Django 5.2.1 on 2025-06-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_course_department_alter_course_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
