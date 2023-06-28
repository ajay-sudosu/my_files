from nis import cat
from re import L
from django.shortcuts import render
from httplib2 import Response
from sqlalchemy import true
from .models import Category,Quiz,Question
from .serializer import CategorySerializer,QuizSerializer,QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Category_class(APIView):
    def get(self,request,format=None,pk=None):
        id = pk
        if pk is not None:
            quiz_obj = Category.objects.get(id=id)
            serializer = CategorySerializer(quiz_obj)
            return Response(serializer.data)
        quiz_obj = Category.objects.all()
        serializer = CategorySerializer(quiz_obj,many=True)
        return Response(serializer.data)

class Quiz_class(APIView):
    def get(self,request,format=None,pk=None):
        id = pk
        if id is not None:
            cat_obj = Category.objects.get(id=id)
            print(cat_obj)
            print(cat_obj.category.get(id=id))
            print('--------------------------')
            quiz_obj = Quiz.objects.get(id=id)
            print(quiz_obj.category)    
            print(quiz_obj.date_created)  
            print(quiz_obj.title) 
            serializer = QuizSerializer(quiz_obj) 
            return Response(serializer.data)
        quiz_obj = Quiz.objects.all()  
        serializer = QuizSerializer(quiz_obj,many=True)
        return Response(serializer.data)
        
