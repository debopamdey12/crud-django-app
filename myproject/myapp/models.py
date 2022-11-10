from django.db import models

# Create your models here.
class Employees(models.Model):
    Name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    address=models.TextField()
    phone=models.IntegerField()
    def __str__(self) :
        return self.Name
