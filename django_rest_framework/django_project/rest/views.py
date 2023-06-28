from .models import Student
from django.shortcuts import render
from .serializer import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(["GET","POST","DELETE","PUT","PATCH"])
def student_api(request,pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            stu_obj = Student.objects.get(id=id)
            serializer = StudentSerializer(stu_obj)
            return Response(serializer.data)
        stu_obj =  Student.objects.all()
        serializer = StudentSerializer(stu_obj,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        print(request.data)
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

        return Response({'messaege':'data added successfully'})

    elif request.method == "PUT":
        print(request.data)
        id = pk
        stu_obj = Student.objects.get(id=id)
        data = request.data
        serializer = StudentSerializer(stu_obj,data=data)
        if serializer.is_valid():
            serializer.save()

        return Response({'messaege':'data added successfully'})


    elif request.method == "DELETE":
        id = pk
        stu_obj = Student.objects.get(id=id)
        stu_obj.delete()
        return Response({"message":"data deleted successfuly"})