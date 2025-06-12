from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

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


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course-details.html'
    context_object_name = 'course'


class CourseAddView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/add-course.html'
    success_url = reverse_lazy('courses')

    def form_valid(self, form):
        messages.success(self.request, 'Course created successfully.')
        return super().form_valid(form)


class CourseEditView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/edit-course.html'
    context_object_name = 'course'
    success_url = reverse_lazy('courses')

    def form_valid(self, form):
        messages.success(self.request, 'Course updated successfully.')
        return super().form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/delete-course.html'
    context_object_name = 'course'
    success_url = reverse_lazy('courses')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Course deleted successfully.')
        return super().delete(request, *args, **kwargs)


# --------------- DEPARTMENTS VIEWS --------------------
class DepartmentsListView(ListView):
    model = Department
    template_name = 'departments/departments.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/department-details.html'
    context_object_name = 'department'


class DepartmentAddView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/add-department.html'
    success_url = reverse_lazy('departments')

    def form_valid(self, form):
        messages.success(self.request, 'Department created successfully.')
        return super().form_valid(form)


class DepartmentEditView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/edit-department.html'
    context_object_name = 'department'
    success_url = reverse_lazy('departments')

    def form_valid(self, form):
        messages.success(self.request, 'Department updated successfully.')
        return super().form_valid(form)


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'departments/delete-department.html'
    context_object_name = 'department'
    success_url = reverse_lazy('departments')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Department deleted successfully.')
        return super().delete(request, *args, **kwargs)


# --------------- TEACHERS VIEWS --------------------
class TeachersListView(ListView):
    model = Teacher
    template_name = 'teachers/teachers.html'
    context_object_name = 'teachers'


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/teacher-details.html'
    context_object_name = 'teacher'


class TeacherAddView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/add-teacher.html'
    success_url = reverse_lazy('teachers')

    def form_valid(self, form):
        messages.success(self.request, 'Teacher created successfully.')
        return super().form_valid(form)


class TeacherEditView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/edit-teacher.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('teachers')

    def form_valid(self, form):
        messages.success(self.request, 'Teacher updated successfully.')
        return super().form_valid(form)


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers/delete-teacher.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('teachers')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Teacher deleted successfully.')
        return super().delete(request, *args, **kwargs)


# --------------- STUDENTS VIEWS --------------------
class StudentsListView(ListView):
    model = Student
    template_name = 'students/students.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student-details.html'
    context_object_name = 'student'


class StudentAddView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/add-student.html'
    success_url = reverse_lazy('students')

    def form_valid(self, form):
        messages.success(self.request, 'Student created successfully.')
        return super().form_valid(form)


class StudentEditView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/edit-student.html'
    context_object_name = 'student'
    success_url = reverse_lazy('students')

    def form_valid(self, form):
        messages.success(self.request, 'Student updated successfully.')
        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/delete-student.html'
    context_object_name = 'student'
    success_url = reverse_lazy('students')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Student deleted successfully.')
        return super().delete(request, *args, **kwargs)


# --------------- FACULTIES VIEWS --------------------
class FacultiesListView(ListView):
    model = Faculty
    template_name = 'faculties/faculties.html'
    context_object_name = 'faculties'


class FacultyDetailView(DetailView):
    model = Faculty
    template_name = 'faculties/faculty-details.html'
    context_object_name = 'faculty'


class FacultyAddView(CreateView):
    model = Faculty
    form_class = FacultyForm
    template_name = 'faculties/add-faculty.html'
    success_url = reverse_lazy('faculties')

    def form_valid(self, form):
        messages.success(self.request, 'Faculty created successfully.')
        return super().form_valid(form)


class FacultyEditView(UpdateView):
    model = Faculty
    form_class = FacultyForm
    template_name = 'faculties/edit-faculty.html'
    context_object_name = 'faculty'
    success_url = reverse_lazy('faculties')

    def form_valid(self, form):
        messages.success(self.request, 'Faculty updated successfully.')
        return super().form_valid(form)


class FacultyDeleteView(DeleteView):
    model = Faculty
    template_name = 'faculties/delete-faculty.html'
    context_object_name = 'faculty'
    success_url = reverse_lazy('faculties')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Faculty deleted successfully.')
        return super().delete(request, *args, **kwargs)


# --------------- PROGRAMS VIEWS --------------------
class ProgramsListView(ListView):
    model = SemesterProgram
    template_name = 'programs/programs.html'
    context_object_name = 'programs'


class ProgramDetailView(DetailView):
    model = SemesterProgram
    template_name = 'programs/program-details.html'
    context_object_name = 'program'


class ProgramAddView(CreateView):
    model = SemesterProgram
    form_class = SemesterProgramForm
    template_name = 'programs/add-program.html'
    success_url = reverse_lazy('programs')

    def form_valid(self, form):
        messages.success(self.request, 'Program created successfully.')
        return super().form_valid(form)


class ProgramEditView(UpdateView):
    model = SemesterProgram
    form_class = SemesterProgramForm
    template_name = 'programs/edit-program.html'
    context_object_name = 'program'
    success_url = reverse_lazy('programs')

    def form_valid(self, form):
        messages.success(self.request, 'Program updated successfully.')
        return super().form_valid(form)


class ProgramDeleteView(DeleteView):
    model = SemesterProgram
    template_name = 'programs/delete-program.html'
    context_object_name = 'program'
    success_url = reverse_lazy('programs')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Program deleted successfully.')
        return super().delete(request, *args, **kwargs)


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


# --------------- COLLEGE VIEWS --------------------
class CollegesListView(ListView):
    model = College
    template_name = 'colleges/colleges.html'
    context_object_name = 'colleges'


class CollegeDetailView(DetailView):
    model = College
    template_name = 'colleges/college-details.html'
    context_object_name = 'college'


class CollegeAddView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'colleges/add-college.html'
    success_url = reverse_lazy('colleges')

    def form_valid(self, form):
        messages.success(self.request, 'College created successfully.')
        return super().form_valid(form)


class CollegeEditView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'colleges/edit-college.html'
    context_object_name = 'college'
    success_url = reverse_lazy('colleges')

    def form_valid(self, form):
        messages.success(self.request, 'College updated successfully.')
        return super().form_valid(form)


class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'colleges/delete-college.html'
    context_object_name = 'college'
    success_url = reverse_lazy('colleges')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'College deleted successfully.')
        return super().delete(request, *args, **kwargs)


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
