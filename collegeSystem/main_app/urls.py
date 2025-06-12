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
    path('courses/add-course/', CourseAddView.as_view(), name='add-course'),
    path('courses/edit-course/<int:pk>/', CourseEditView.as_view(), name='edit-course'),
    path('courses/delete-course/<int:pk>/', CourseDeleteView.as_view(), name='delete-course'),

    # --------------- DEPARTMENTS URLS --------------------
    path('departments/', DepartmentsListView.as_view(), name='departments'),
    path('departments/department-details/<int:pk>/', DepartmentDetailView.as_view(), name='department-details'),
    path('departments/add-department/', DepartmentAddView.as_view(), name='add-department'),
    path('departments/edit-department/<int:pk>/', DepartmentEditView.as_view(), name='edit-department'),
    path('departments/delete-department/<int:pk>/', DepartmentDeleteView.as_view(), name='delete-department'),

    # --------------- TEACHERS URLS --------------------
    path('teachers/', TeachersListView.as_view(), name='teachers'),
    path('teachers/teacher-details/<int:pk>/', TeacherDetailView.as_view(), name='teacher-details'),
    path('teachers/add-teacher/', TeacherAddView.as_view(), name='add-teacher'),
    path('teachers/edit-teacher/<int:pk>/', TeacherEditView.as_view(), name='edit-teacher'),
    path('teachers/delete-teacher/<int:pk>/', TeacherDeleteView.as_view(), name='delete-teacher'),

    # --------------- STUDENTS URLS --------------------
    path('students/', StudentsListView.as_view(), name='students'),
    path('students/student-details/<int:pk>/', StudentDetailView.as_view(), name='student-details'),
    path('students/add-student/', StudentAddView.as_view(), name='add-student'),
    path('students/edit-student/<int:pk>/', StudentEditView.as_view(), name='edit-student'),
    path('students/delete-student/<int:pk>/', StudentDeleteView.as_view(), name='delete-student'),

    # --------------- FACULTIES URLS --------------------
    path('faculties/', FacultiesListView.as_view(), name='faculties'),
    path('faculties/faculty-details/<int:pk>/', FacultyDetailView.as_view(), name='faculty-details'),
    path('faculties/add-faculty/', FacultyAddView.as_view(), name='add-faculty'),
    path('faculties/edit-faculty/<int:pk>/', FacultyEditView.as_view(), name='edit-faculty'),
    path('faculties/delete-faculty/<int:pk>/', FacultyDeleteView.as_view(), name='delete-faculty'),

    # --------------- PROGRAMS URLS --------------------
    path('programs/', ProgramsListView.as_view(), name='programs'),
    path('programs/program-details/<int:pk>/', ProgramDetailView.as_view(), name='program-details'),
    path('programs/student-program/<int:pk>/', StudentProgramView.as_view(), name='student-program'),
    path('programs/add-program/', ProgramAddView.as_view(), name='add-program'),
    path('programs/edit-program/<int:pk>/', ProgramEditView.as_view(), name='edit-program'),
    path('programs/delete-program/<int:pk>/', ProgramDeleteView.as_view(), name='delete-program'),

    # --------------- COLLEGES URLS --------------------
    path('colleges/', CollegesListView.as_view(), name='colleges'),
    path('colleges/college-details/<int:pk>/', CollegeDetailView.as_view(), name='college-details'),
    path('colleges/add-college/', CollegeAddView.as_view(), name='add-college'),
    path('colleges/edit-college/<int:pk>/', CollegeEditView.as_view(), name='edit-college'),
    path('colleges/delete-college/<int:pk>/', CollegeDeleteView.as_view(), name='delete-college'),

    # --------------- ENROLLMENTS URLS --------------------
    path('enrollments/', EnrollmentsListView.as_view(), name='enrollments'),
    path('enrollments/enrollment-details/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment-details'),
    path('enrollments/add-enrollment/', EnrollmentAddView.as_view(), name='add-enrollment'),
    path('enrollments/edit-enrollment/<int:pk>/', EnrollmentEditView.as_view(), name='edit-enrollment'),
    path('enrollments/delete-enrollment/<int:pk>/', EnrollmentDeleteView.as_view(), name='delete-enrollment'),

    # --------------- GRADES URLS --------------------
    path('grades/', GradesListView.as_view(), name='grades'),
    path('grades/add-grade/', GradeAddView.as_view(), name='add-grade'),
    path('grades/edit-grade/<int:pk>/', GradeEditView.as_view(), name='edit-grade'),
    path('grades/delete-grade/<int:pk>/', GradeDeleteView.as_view(), name='delete-grade'),

    # --------------- STATISTICS URLS --------------------
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]