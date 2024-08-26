from django.urls import path 
from .views import StudentsView ,add, StudentView  , remove,  index ,  update
urlpatterns = [
    path("student/<int:id>" , StudentView.as_view()) ,
    path("student" , StudentsView.as_view()) , 
    path("" , index) ,
    path("update/<int:id>" , update) ,
    path("remove/<int:id>" , remove) , 
    path("add" , add) 
]
