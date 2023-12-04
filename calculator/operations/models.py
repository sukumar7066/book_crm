from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=100)
    department=models.CharField(max_length=100)

    def __str__(self): 
        return  self.name  
    
class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication=models.PositiveIntegerField(null=True)

class Mobile(models.Model):
     
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    price = models.CharField(max_length=20)
    color = models.CharField(max_length=50)



  


