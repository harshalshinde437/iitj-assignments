from django.db import models

# Create your models here.

class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.roll_number
