from django.db import models

# Create your models here.
class Jobs(models.Model):
    Title = models.CharField(max_length=250)
    Location = models.CharField(max_length=250)
    Company = models.CharField(max_length=250)
    Salary = models.CharField(max_length=250)
    Date = models.CharField(max_length=250)
    Description = models.CharField(max_length=1500)
