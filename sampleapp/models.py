from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.TextField()
    number=models.IntegerField()
    password=models.CharField(max_length=12)
    confirmpassword=models.CharField(max_length=12)

class Contact(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    subject=models.TextField()
    message=models.TextField()

class Schedule(models.Model):
    user=models.ForeignKey(Signup,on_delete=models.CASCADE)
    time=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    
class Complaint(models.Model):
    subject=models.TextField()
    message=models.TextField()


    