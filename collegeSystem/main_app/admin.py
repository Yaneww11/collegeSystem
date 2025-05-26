from django.contrib import admin
from .models import (
    College,
    Faculty,
    Department,
    Enrollment,
    SemesterProgram,
    Course,
    Grade,
    Student,
    Teacher
)

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'rector', 'created_at', 'updated_at')
    search_fields = ('name', 'address')

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'college')
    search_fields = ('name',)
    list_filter = ('college',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'head')
    search_fields = ('name',)
    list_filter = ('faculty',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at', 'status')
    list_filter = ('status',)
    search_fields = ('student__profile__user__username', 'course__name')

@admin.register(SemesterProgram)
class SemesterProgramAdmin(admin.ModelAdmin):
    list_display = ('semester', 'year', 'college')
    list_filter = ('year', 'college')
    search_fields = ('semester',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'teacher', 'semester_program')
    search_fields = ('name', 'description')
    list_filter = ('department', 'semester_program')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'teacher', 'value', 'issued_at')
    search_fields = ('student__profile__user__username', 'course__name')
    list_filter = ('teacher', 'course')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('profile', 'specialty')
    search_fields = ('profile__user__username', 'specialty')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('profile', 'department')
    search_fields = ('profile__user__username', 'description')
    list_filter = ('department',)
