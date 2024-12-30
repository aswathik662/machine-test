from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    date_of_joining=models.DateField()
    salary=models.FloatField()
    profile_image=models.ImageField(upload_to='image/')