from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    College,
    Faculty,
    Department,
    Enrollment,
    SemesterProgram,
    Course,
    Student,
    Teacher
)

@admin.register(College)
class CollegeAdmin(ModelAdmin):
    list_display = ('name', 'rector', 'created_at', 'updated_at')
    search_fields = ('name', 'address')

@admin.register(Faculty)
class FacultyAdmin(ModelAdmin):
    list_display = ('name', 'college', 'head',)
    search_fields = ('name', 'head__profile__user__username')
    list_filter = ('college', 'head')

@admin.register(Department)
class DepartmentAdmin(ModelAdmin):
    list_display = ('name', 'faculty', 'head')
    search_fields = ('name',)
    list_filter = ('faculty',)

@admin.register(Enrollment)
class EnrollmentAdmin(ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at', 'status')
    list_filter = ('status',)
    search_fields = ('student__profile__user__username', 'course__name')

@admin.register(SemesterProgram)
class SemesterProgramAdmin(ModelAdmin):
    list_display = ('semester', 'year', 'department')
    list_filter = ('year', 'department')
    search_fields = ('semester',)

@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ('name', 'department', 'teacher', 'semester_program')
    search_fields = ('name', 'description')
    list_filter = ('department', 'semester_program')

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    list_display = ('profile',)
    search_fields = ('profile__user__username', )

@admin.register(Teacher)
class TeacherAdmin(ModelAdmin):
    list_display = ('profile', 'department', 'faculty')
    search_fields = ('profile__user__username', 'description', 'faculty__name')
    list_filter = ('department',)
