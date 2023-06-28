from django.shortcuts import render
from itsdangerous import serializer
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student
from.serializer import StudentSerializer

# Create your views here.

class Student_LC(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    

class Student_RUD(UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def put(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return self.put(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
