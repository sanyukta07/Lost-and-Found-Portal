from django.db import models




# Create your models here.
class Student(models.Model):
    Fullname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.BigIntegerField()
    Lostdate=models.DateField()
    Lastseen=models.CharField(max_length=50)
    Description=models.CharField(max_length=50 ,default='some string')

class User(models.Model):
    Fullname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.BigIntegerField()
    Course=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
   
class Found(models.Model):
    Fullname=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Contact=models.BigIntegerField()
    Foundplace=models.CharField(max_length=50)
    Foundon=models.DateField()
    Image=models.ImageField(upload_to="img/")
    



