from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics



class StudentList(generics.ListAPIView):
        serializer_class=StudentSerializer
        queryset = Student.objects.all()

class StudentCreate(generics.ListCreateAPIView):
        serializer_class=StudentSerializer
        queryset = Student.objects.all()

class StudentUpdate(generics.UpdateAPIView):
        serializer_class=StudentSerializer
        queryset = Student.objects.all()


class StudentDelete(generics.DestroyAPIView):
        serializer_class=StudentSerializer
        queryset = Student.objects.all()


        


#   
# Create your views here.
