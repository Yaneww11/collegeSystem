from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db import transaction

from .models import (
    College, Faculty, Department, Course, Student, Teacher,
    SemesterProgram, Enrollment, Grade
)
from .forms import (
    CollegeForm, FacultyForm, DepartmentForm, CourseForm, StudentForm, TeacherForm,
    SemesterProgramForm, EnrollmentForm, GradeForm
)


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


# --------------- COURSES VIEWS --------------------
class CoursesListView(ListView):
    model = Course
    template_name = 'courses/courses.html'
    context_object_name = 'courses'
    # update this to pass courses based on logged-in user + role
    # if student, show only courses they are enrolled in and remove manage action button
    # if teacher, show only courses they teach


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course-details.html'
    context_object_name = 'course'

class CourseManageView(DetailView):
    model = Course
    template_name = 'courses/course-manage.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        print(context)
        context['options'] = "2,3,4,5,6,None".split(',')
        return context
    
    def post(self, request, *args, **kwargs):
        course = self.get_object()
        enrollments = course.enrollments.select_related('student')

        with transaction.atomic():
            for enrollment in enrollments:
                student_id = enrollment.student.id

                #Handle grade
                grade_value = request.POST.get(f'grade_{student_id}')
                if grade_value and grade_value != 'None':
                    grade_object, created = Grade.objects.get_or_create(
                        student=enrollment.student,
                        course=course,
                        defaults={'value': grade_value}
                    )
                    if not created:
                        grade_object.value = grade_value
                        grade_object.save()
                else:
                    # If grade is selected as None, delete the grade
                    Grade.objects.filter(student=enrollment.student, course=course).delete()

                # Handle absences
                absences_val = request.POST.get(f'absences_{student_id}')
                if absences_val is not None:
                    try:
                        enrollment.absences = int(absences_val)
                        enrollment.save()
                    except ValueError:
                        pass  # Optionally handle invalid input, shouldn't happen

        messages.success(request, 'Changes saved successfully.')
        return redirect('course-manage', pk=course.pk)

# --------------- DEPARTMENTS VIEWS --------------------
class DepartmentsListView(ListView):
    model = Department
    template_name = 'departments/departments.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/department-details.html'
    context_object_name = 'department'



# --------------- TEACHERS VIEWS --------------------
class TeachersListView(ListView):
    model = Teacher
    template_name = 'teachers/teachers.html'
    context_object_name = 'teachers'


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/teacher-details.html'
    context_object_name = 'teacher'



# --------------- STUDENTS VIEWS --------------------
class StudentsListView(ListView):
    model = Student
    template_name = 'students/students.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student-details.html'
    context_object_name = 'student'





# --------------- FACULTIES VIEWS --------------------
class FacultiesListView(ListView):
    model = Faculty
    template_name = 'faculties/faculties.html'
    context_object_name = 'faculties'


class FacultyDetailView(DetailView):
    model = Faculty
    template_name = 'faculties/faculty-details.html'
    context_object_name = 'faculty'





# --------------- PROGRAMS VIEWS --------------------
class ProgramsListView(ListView):
    model = SemesterProgram
    template_name = 'programs/programs.html'
    context_object_name = 'programs'
    # update this to somehow show the courses the student can enroll in


class ProgramDetailView(DetailView):
    model = SemesterProgram
    template_name = 'programs/program-details.html'
    context_object_name = 'program'





class StudentProgramView(ListView):
    model = Course
    template_name = 'programs/student-program.html'
    context_object_name = 'courses'

    def get_queryset(self):
        student_id = self.kwargs.get('pk')
        return Course.objects.filter(students__pk=student_id)


# --------------- STATISTICS VIEWS --------------------
class StatisticsView(TemplateView):
    template_name = 'statistics/statistics.html'



# --------------- ENROLLMENT VIEWS --------------------
class EnrollmentsListView(ListView):
    model = Enrollment
    template_name = 'enrollments/enrollments.html'
    context_object_name = 'enrollments'


class EnrollmentDetailView(DetailView):
    model = Enrollment
    template_name = 'enrollments/enrollment-details.html'
    context_object_name = 'enrollment'


class EnrollmentAddView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/add-enrollment.html'
    success_url = reverse_lazy('enrollments')

    def form_valid(self, form):
        messages.success(self.request, 'Enrollment created successfully.')
        return super().form_valid(form)


class EnrollmentEditView(UpdateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/edit-enrollment.html'
    context_object_name = 'enrollment'
    success_url = reverse_lazy('enrollments')

    def form_valid(self, form):
        messages.success(self.request, 'Enrollment updated successfully.')
        return super().form_valid(form)


class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'enrollments/delete-enrollment.html'
    context_object_name = 'enrollment'
    success_url = reverse_lazy('enrollments')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Enrollment deleted successfully.')
        return super().delete(request, *args, **kwargs)


# --------------- GRADE VIEWS --------------------
class GradesListView(ListView):
    model = Grade
    template_name = 'grades/grades.html'
    context_object_name = 'grades'


class GradeAddView(CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'grades/add-grade.html'
    success_url = reverse_lazy('grades')

    def form_valid(self, form):
        messages.success(self.request, 'Grade created successfully.')
        return super().form_valid(form)


class GradeEditView(UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = 'grades/edit-grade.html'
    context_object_name = 'grade'
    success_url = reverse_lazy('grades')

    def form_valid(self, form):
        messages.success(self.request, 'Grade updated successfully.')
        return super().form_valid(form)


class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'grades/delete-grade.html'
    context_object_name = 'grade'
    success_url = reverse_lazy('grades')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Grade deleted successfully.')
        return super().delete(request, *args, **kwargs)
