from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class course(models.Model):
    coursename=models.CharField(max_length=255)
    fees=models.IntegerField()
class addstud(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    address=models.CharField(max_length=255)
    joining_date=models.DateField()
    phone_no=models.IntegerField()
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
class teacheruser(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    number=models.CharField(max_length=255)
    image=models.ImageField(default="default1.jpg",blank=True,upload_to="image/", null=True)