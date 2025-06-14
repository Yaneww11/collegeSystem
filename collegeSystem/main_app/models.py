from django.contrib.auth.models import User
from django.db import models

from collegeSystem.users.models import Profile


class College(models.Model):
    name = models.CharField(
        max_length=255
    )

    address = models.TextField()

    rector = models.OneToOneField(
        to=Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(
        max_length=255
    )

    college = models.ForeignKey(
        to='College',
        on_delete=models.CASCADE,
        related_name='faculties',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(
        max_length=255
    )

    faculty = models.ForeignKey(
        to='Faculty',
        on_delete=models.CASCADE,
        related_name='departments',
        null=True,
        blank=True,
    )

    head = models.OneToOneField(
        to='Teacher',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='head_of_department'
    )

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(
        to='Student',
        on_delete=models.CASCADE,
        related_name='enrollments',
        null=True,
        blank=True,
    )

    course = models.ForeignKey(
        to='Course',
        on_delete=models.CASCADE,
        related_name='enrollments',
        null=True,
        blank=True,
    )

    enrolled_at = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=[('active', 'Active'), ('dropped', 'Dropped'), ('completed', 'Completed')]
    )

    absences = models.PositiveIntegerField(default=0)

    grade = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    class Meta:
        unique_together = (('student', 'course'),)

    def __str__(self):
        return f"{self.student} - {self.course} ({self.status})"


class SemesterProgram(models.Model):
    semester = models.CharField(
        max_length=20
    )

    year = models.PositiveIntegerField()

    college = models.ForeignKey( # change to department?
        to='College',
        on_delete=models.CASCADE,
        related_name='semester_programs',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.semester} {self.year}"


class Course(models.Model):
    name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    credits = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    department = models.ForeignKey(
        to='Department',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='courses'
    )

    teacher = models.ForeignKey(
        to='Teacher',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='courses'
    )

    semester_program = models.ForeignKey(
        to='SemesterProgram',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='courses',
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='student_profile'
    )

    enrolled_courses = models.ManyToManyField(
        to='Course',
        through='Enrollment',
        related_name='students'
    )

    enrolled_program = models.ForeignKey(
        to='SemesterProgram',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )

    def __str__(self):
        return self.profile.user.get_full_name()


class Teacher(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='teacher_profile'
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

    def __str__(self):
        return self.profile.user.get_full_name()
