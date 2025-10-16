from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    insurance = models.CharField(max_length=100)