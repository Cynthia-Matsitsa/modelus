from django.shortcuts import render
from django.shortcuts import render
from api.serializer import Class_PeriodSerializer, CourseSerializer, ClassroomSerializer, StudentSerializer, TeacherSerializer
from classperiod.models import Class_Period
from classroom.models import Classroom
from course.models import Courses
from student.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from teacher.models import Teacher
from rest_framework import status
# Create your views here.
class StudentListViews(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
class TeacherListViews(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
class CourseListViews(APIView):
    def get(self, request):
        course = Courses.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
class ClassroomListViews(APIView):
    def get(self, request):
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many=True)
        return Response(serializer.data)
class Class_PeriodListViews(APIView):
    def get(self, request):
        class_period = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(class_period, many=True)
        return Response(serializer.data)

class StudentListViews(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=...)
        return Response(serializer)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializerdata,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class StudentDetailsView(APIView):
    def get(self,request,id):
        student = Student.objects.opt(id=id)
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    
class StudentDetailsView(APIView):
    def put(self,request,id):
        student = Student.objects.opt(id=id)
        serializer=StudentSerializer(student)
        return Response(serializer.datastatus)
        
  
    
    
                
    
    
    
    
        
    
     