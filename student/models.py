from django.db import models

# Create your models here.

class Student(models.Model) :
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField() 
    email = models.EmailField(max_length=254)
    url = models.URLField(max_length=100)
    class Meta : 
        db_table = "student" 
    def __str__ (self) : 
        return self.first_name + " " + self.last_name 
    @property
    def full_name(self) :
        return self.first_name + " " + self.last_name 

