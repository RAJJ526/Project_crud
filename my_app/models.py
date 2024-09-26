from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    Class=models.IntegerField()
    roll_no=models.IntegerField()
    status=models.CharField(max_length=100)

    
