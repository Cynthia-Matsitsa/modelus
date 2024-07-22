
from django.urls import path
from api.views import  StudentListViews
from api.views import TeacherListViews
from api.views import CourseListViews
from api.views import StudentDetailsView
from api.views import courseDetailView
from api.views import  teacherDetailView
from .views import classesDetailView  
from .views import ClassesListView 

urlpatterns = [
    path("Student/",StudentListViews.as_view(),name = "student_list_view"),
    path("Teacher/",TeacherListViews.as_view(),name = "teacher_list_view"),
    path("Courses/",CourseListViews.as_view(),name = "course_list_view"),
     path("Students/",StudentDetailsView.as_view(),name = "student_list_view"),
     path("classes/<int:id>/",classesDetailView.as_view(),name="Course_detail_view"),
     path("classes/",ClassesListView.as_view(),name="classes_list_view"), 
    
]
