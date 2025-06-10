from django.shortcuts import render
from django.views.generic import ListView, TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


# --------------- COURSES VIEWS --------------------
class CoursesListView(TemplateView):
    template_name = 'courses/courses.html'


class CourseDetailView(TemplateView):
    template_name = 'courses/course-details.html'


class CourseAddView(TemplateView):
    template_name = 'courses/add-course.html'


class CourseEditView(TemplateView):
    template_name = 'courses/edit-course.html'


class CourseDeleteView(TemplateView):
    template_name = 'courses/delete-course.html'


# --------------- DEPARTMENTS VIEWS --------------------
class DepartmentsListView(TemplateView):
    template_name = 'departments/departments.html'


class DepartmentDetailView(TemplateView):
    template_name = 'departments/department-details.html'


class DepartmentAddView(TemplateView):
    template_name = 'departments/add-department.html'


class DepartmentEditView(TemplateView):
    template_name = 'departments/edit-department.html'


class DepartmentDeleteView(TemplateView):
    template_name = 'departments/delete-department.html'


# --------------- TEACHERS VIEWS --------------------
class TeachersListView(TemplateView):
    template_name = 'teachers/teachers.html'


class TeacherDetailView(TemplateView):
    template_name = 'teachers/teacher-details.html'


class TeacherAddView(TemplateView):
    template_name = 'teachers/add-teacher.html'


class TeacherEditView(TemplateView):
    template_name = 'teachers/edit-teacher.html'


class TeacherDeleteView(TemplateView):
    template_name = 'teachers/delete-teacher.html'


# --------------- STUDENTS VIEWS --------------------
class StudentsListView(TemplateView):
    template_name = 'students/students.html'


class StudentDetailView(TemplateView):
    template_name = 'students/student-details.html'


class StudentAddView(TemplateView):
    template_name = 'students/add-student.html'


class StudentEditView(TemplateView):
    template_name = 'students/edit-student.html'


class StudentDeleteView(TemplateView):
    template_name = 'students/delete-student.html'


# --------------- FACULTIES VIEWS --------------------
class FacultiesListView(TemplateView):
    template_name = 'faculties/faculties.html'


class FacultyDetailView(TemplateView):
    template_name = 'faculties/faculty-details.html'


class FacultyAddView(TemplateView):
    template_name = 'faculties/add-faculty.html'


class FacultyEditView(TemplateView):
    template_name = 'faculties/edit-faculty.html'


class FacultyDeleteView(TemplateView):
    template_name = 'faculties/delete-faculty.html'


# --------------- PROGRAMS VIEWS --------------------
class ProgramsListView(TemplateView):
    template_name = 'programs/programs.html'


class ProgramDetailView(TemplateView):
    template_name = 'programs/program-details.html'


class ProgramAddView(TemplateView):
    template_name = 'programs/add-program.html'


class StudentProgramView(TemplateView):
    template_name = 'programs/student-program.html'


class ProgramEditView(TemplateView):
    template_name = 'programs/edit-program.html'


class ProgramDeleteView(TemplateView):
    template_name = 'programs/delete-program.html'


# --------------- STATISTICS VIEWS --------------------
class StatisticsView(TemplateView):
    template_name = 'statistics/statistics.html'