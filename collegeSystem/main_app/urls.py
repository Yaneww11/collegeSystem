from django.urls import path, include

from collegeSystem.main_app.views import HomeView, CoursesListView, CourseAddView, CourseDetailView, CourseEditView, \
    CourseDeleteView, DepartmentsListView, DepartmentDetailView, DepartmentAddView, DepartmentEditView, \
    DepartmentDeleteView, TeachersListView, TeacherDetailView, TeacherAddView, TeacherEditView, TeacherDeleteView, \
    StudentsListView, StudentDetailView, StudentAddView, StudentEditView, StudentDeleteView, FacultiesListView, \
    FacultyDetailView, FacultyAddView, FacultyEditView, FacultyDeleteView, ProgramsListView, ProgramDetailView, \
    StudentProgramView, ProgramAddView, ProgramEditView, ProgramDeleteView, StatisticsView, CollegesListView, \
    CollegeDetailView, CollegeAddView, CollegeEditView, CollegeDeleteView, EnrollmentsListView, EnrollmentDetailView, \
    EnrollmentAddView, EnrollmentEditView, EnrollmentDeleteView, GradesListView, GradeAddView, GradeEditView, \
    GradeDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # ---------------- COURSES URLS ---------------------
    path('courses/', CoursesListView.as_view(), name='courses'),
    path('courses/course-details/<int:pk>/', CourseDetailView.as_view(), name='course-details'),

    # --------------- DEPARTMENTS URLS --------------------
    path('departments/', DepartmentsListView.as_view(), name='departments'),
    path('departments/department-details/<int:pk>/', DepartmentDetailView.as_view(), name='department-details'),

    # --------------- TEACHERS URLS --------------------
    path('teachers/', TeachersListView.as_view(), name='teachers'),
    path('teachers/teacher-details/<int:pk>/', TeacherDetailView.as_view(), name='teacher-details'),

    # --------------- STUDENTS URLS --------------------
    path('students/', StudentsListView.as_view(), name='students'),
    path('students/student-details/<int:pk>/', StudentDetailView.as_view(), name='student-details'),

    # --------------- FACULTIES URLS --------------------
    path('faculties/', FacultiesListView.as_view(), name='faculties'),
    path('faculties/faculty-details/<int:pk>/', FacultyDetailView.as_view(), name='faculty-details'),

    # --------------- PROGRAMS URLS --------------------
    path('programs/', ProgramsListView.as_view(), name='programs'),
    path('programs/program-details/<int:pk>/', ProgramDetailView.as_view(), name='program-details'),
    path('programs/student-program/<int:pk>/', StudentProgramView.as_view(), name='student-program'),

    # --------------- COLLEGES URLS --------------------
    path('colleges/', CollegesListView.as_view(), name='colleges'),
    path('colleges/college-details/<int:pk>/', CollegeDetailView.as_view(), name='college-details'),

    # --------------- ENROLLMENTS URLS --------------------
    path('enrollments/', EnrollmentsListView.as_view(), name='enrollments'),
    path('enrollments/enrollment-details/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment-details'),

    # --------------- GRADES URLS --------------------
    path('grades/', GradesListView.as_view(), name='grades'),

    # --------------- STATISTICS URLS --------------------
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]