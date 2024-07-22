from django.shortcuts import render
from django.shortcuts import render
from akirachix.teacher.apps import TeacherConfig
from api.serializer import CourseSerializer, ClassesSerializer, StudentSerializer, TeacherSerializer

from course.models import Course
from student.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import status
from classes.models import models
class StudentListViews(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
class TeacherListViews(APIView):
    def get(self, request):
        teacher = TeacherConfig.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
class CourseListViews(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
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
            return Response(serializer.data,status=status.HTTP_201_CREATED)
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
    
def delete(self,request,id):
      Classroom= Classroom.objects.get(id=id)
      Classroom.delete()
      return Response(status=status.HTTP_202_ACCEPTED)


  
class courseDetailView(APIView):
    def get(self,request,id):
        Course=Course.objects.all.get(id=id)
        serializer =CourseSerializer(Course)
        return Response(serializer.data)
    
    def put(self,request,id):
        Course= Course.objects.get(id=id)
        serializer=CourseSerializer(Course,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
      Course= Course.objects.get(id=id)
      Course.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
  
class teacherDetailView(APIView):
    def get(self,request,id):
        Teacher=Teacher.objects.all.get(id=id)
        serializer =CourseSerializer(Teacher)
        return Response(serializer.data)
    
    def put(self,request,id):
        Teacher= Teacher.objects.get(id=id)
        serializer=TeacherSerializer(Teacher,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
      Teacher= Teacher.objects.get(id=id)
      Teacher.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
  
    class classesDetailView(APIView):
      def get(self,request,id):
        Classes=Classes.objects.all.get(id=id)
        serializer = ClassesSerializer(Classes)
        return Response(serializer.data)
    def put(self,request,id):
        Classes= Classes.objects.get(id=id)
        serializer= ClassesSerializer(Classes,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
      Classes= Classes.objects.get(id=id)
      Classes.delete()
      return Response(status=status.HTTP_202_ACCEPTED) 

  
  
  
    
  
    
    
                
    
    
    
    
        
    
     