from django.db import models

# Create your models here.
class SData(models.Model):
     sname=models.CharField(max_length=30)
     sage=models.IntegerField()
     smobile=models.IntegerField()
