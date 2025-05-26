from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^(\+359|0)?8[789]\d{7}$',
                message='Please correct valid phone number'
            )
        ],
        help_text='089999999',
    )


# class Rector(models.Model):
#     profile = models.OneToOneField(
#         Profile,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     college = models.OneToOneField('College', on_delete=models.CASCADE)
#
#
# class Student(models.Model):
#     profile = models.OneToOneField(
#         Profile,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     specialty  = models.CharField(max_length=255)
#     enrolled_courses = models.ManyToManyField(
#         'Course',
#         through='Enrollment',
#         related_name='students'
#     )
#
# class Teacher(models.Model):
#     profile = models.OneToOneField(
#         Profile,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     department = models.ForeignKey(
#         'Department',
#         on_delete=models.CASCADE
#     )
#     description = models.TextField(
#         blank=True,
#         null=True
#     )
