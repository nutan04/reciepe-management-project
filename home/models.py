from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField(blank = True ,null =  True)
    address = models.TextField(blank = True ,null =  True)
    image = models.ImageField()
    file = models.FileField()

class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField()

    def __str__(self):
        return self.car_name
    
     
    

