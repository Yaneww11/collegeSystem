from django.contrib.auth.models import User
from django.db import models

from collegeSystem.users.models import Profile


class College(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    rector = models.OneToOneField(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    college = models.ForeignKey(
        'College',
        on_delete=models.CASCADE,
        related_name='faculties',
    )


class Department(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(
        'Faculty',
        on_delete=models.CASCADE,
        related_name='departments',
    )
    head = models.OneToOneField(
        'Teacher',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='head_of_department'  # Added related_name
    )


class Enrollment(models.Model):
    student = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE,
        related_name='enrollments',
    )
    course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name='enrollments',
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('active', 'Active'), ('dropped', 'Dropped'), ('completed', 'Completed')]
    )

    class Meta:
        unique_together = (('student', 'course'),)


class SemesterProgram(models.Model):
    semester = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    college = models.ForeignKey(
        'College',
        on_delete=models.CASCADE,
        related_name='semester_programs',
    )


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    semester_program = models.ForeignKey('SemesterProgram', on_delete=models.CASCADE)


class Grade(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    issued_at = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    specialty = models.CharField(max_length=255)
    enrolled_courses = models.ManyToManyField(
        'Course',
        through='Enrollment',
        related_name='students'
    )


class Teacher(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='teachers',
    )
    description = models.TextField(
        blank=True,
        null=True
    )
