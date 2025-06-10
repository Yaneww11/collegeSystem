from django.urls import path, include

from collegeSystem.main_app.views import HomeView, CoursesListView, CourseAddView, CourseDetailView, CourseEditView, \
    CourseDeleteView, DepartmentsListView, DepartmentDetailView, DepartmentAddView, DepartmentEditView, \
    DepartmentDeleteView, TeachersListView, TeacherDetailView, TeacherAddView, TeacherEditView, TeacherDeleteView, \
    StudentsListView, StudentDetailView, StudentAddView, StudentEditView, StudentDeleteView, FacultiesListView, \
    FacultyDetailView, FacultyAddView, FacultyEditView, FacultyDeleteView, ProgramsListView, ProgramDetailView, \
    StudentProgramView, ProgramAddView, ProgramEditView, ProgramDeleteView, StatisticsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # ---------------- COURSES URLS ---------------------
    path('courses/', CoursesListView.as_view(), name='courses'),
    path('courses/course-details/', CourseDetailView.as_view(), name='course-details'),
    path('courses/add-course/', CourseAddView.as_view(), name='add-course'),
    path('courses/edit-course/', CourseEditView.as_view(), name='edit-course'),
    path('courses/delete-course/', CourseDeleteView.as_view(), name='delete-course'),

    # --------------- DEPARTMENTS URLS --------------------
    path('departments/', DepartmentsListView.as_view(), name='departments'),
    path('departments/department-details/', DepartmentDetailView.as_view(), name='department-details'),
    path('departments/add-department/', DepartmentAddView.as_view(), name='add-department'),
    path('departments/edit-department/', DepartmentEditView.as_view(), name='edit-department'),
    path('departments/delete-department/', DepartmentDeleteView.as_view(), name='delete-department'),

    # --------------- TEACHERS URLS --------------------
    path('teachers/', TeachersListView.as_view(), name='teachers'),
    path('teachers/teacher-details/', TeacherDetailView.as_view(), name='teacher-details'),
    path('teachers/add-teacher/', TeacherAddView.as_view(), name='add-teacher'),
    path('teachers/edit-teacher/', TeacherEditView.as_view(), name='edit-teacher'),
    path('teachers/delete-teacher/', TeacherDeleteView.as_view(), name='delete-teacher'),

    # --------------- STUDENTS URLS --------------------
    path('students/', StudentsListView.as_view(), name='students'),
    path('students/student-details/', StudentDetailView.as_view(), name='student-details'),
    path('students/add-student/', StudentAddView.as_view(), name='add-student'),
    path('students/edit-student/', StudentEditView.as_view(), name='edit-student'),
    path('students/delete-student/', StudentDeleteView.as_view(), name='delete-student'),

    # --------------- FACULTIES URLS --------------------
    path('faculties/', FacultiesListView.as_view(), name='faculties'),
    path('faculties/faculty-details/', FacultyDetailView.as_view(), name='faculty-details'),
    path('faculties/add-faculty/', FacultyAddView.as_view(), name='add-faculty'),
    path('faculties/edit-faculty/', FacultyEditView.as_view(), name='edit-faculty'),
    path('faculties/delete-faculty/', FacultyDeleteView.as_view(), name='delete-faculty'),

    # --------------- PROGRAMS URLS --------------------
    path('programs/', ProgramsListView.as_view(), name='programs'),
    path('programs/program-details/', ProgramDetailView.as_view(), name='program-details'),
    path('programs/student-program/', StudentProgramView.as_view(), name='student-program'),
    path('programs/add-program/', ProgramAddView.as_view(), name='add-program'),
    path('programs/edit-program/', ProgramEditView.as_view(), name='edit-program'),
    path('programs/delete-program/', ProgramDeleteView.as_view(), name='delete-program'),

    # --------------- STATISTICS URLS --------------------
    path('statistics/', StatisticsView.as_view(), name='statistics'),

]