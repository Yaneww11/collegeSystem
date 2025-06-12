from django import forms
from .models import (
    College, Faculty, Department, Course, Student, Teacher,
    SemesterProgram, Enrollment, Grade
)


class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['name', 'address', 'rector']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'rector': forms.Select(attrs={'class': 'form-select'}),
        }


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'college']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'college': forms.Select(attrs={'class': 'form-select'}),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'faculty', 'head']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'faculty': forms.Select(attrs={'class': 'form-select'}),
            'head': forms.Select(attrs={'class': 'form-select'}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'department', 'teacher', 'semester_program']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'teacher': forms.Select(attrs={'class': 'form-select'}),
            'semester_program': forms.Select(attrs={'class': 'form-select'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile', 'specialty']
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-select'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['department', 'description']
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SemesterProgramForm(forms.ModelForm):
    class Meta:
        model = SemesterProgram
        fields = ['semester', 'year', 'college']
        widgets = {
            'semester': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'college': forms.Select(attrs={'class': 'form-select'}),
        }


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'status']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'course', 'teacher', 'value']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'teacher': forms.Select(attrs={'class': 'form-select'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
