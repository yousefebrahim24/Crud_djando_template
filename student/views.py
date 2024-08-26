from django.shortcuts import render , redirect
from django.views import View
from django.http import JsonResponse
from student.models import Student
import json
# Create your views here.

def update(request , id) :
    if request.method == "GET" : 
        data = Student.objects.filter(id = id).values()[0]
        return render(request , "update.html" , data ) 
    elif request.method == "POST" :
        data = request.POST.dict()
        Student.objects.filter(id = id).update(**data)
        return redirect("/")
def remove(request , id) : 
    if request.method == "GET" :
        return render(request , "delete.html" , {"id" : id} )
    elif request.method == "POST" : 
        Student.objects.filter(id = id).delete() ;
        return redirect("/")
def add(request ) :
    if request.method == "GET" :
        return render(request , "Create.html") 
    elif request.method == "POST" : 
        data = request.POST.dict() 
        Student.objects.create(**data) 
        return redirect("/")


def index(request) :
    data = list(Student.objects.values())
    return render(request , "index.html" , {"data": data})
class StudentsView(View) :
    def get(self , request) :
        data = list(Student.objects.values()) 
        return JsonResponse({"data" : data}) 
    def post(self , request , *args, **kwargs) :
        data = json.loads(request.body)
        Student.objects.create(**data) 
        return JsonResponse({"status" : "added successfully"})
class StudentView(View) :
    def put(self , request , *args, **kwargs) :
        data = json.loads(request.body) 
        Student.objects.filter(id=kwargs['id']).update(**data)
        return JsonResponse({"status" : "updated successfully"})
    def delete(self , requst , *args, **kwargs) :
        Student.objects.filter(id=kwargs['id']).delete() 
        return JsonResponse({"status" : "deleted successfully"})





