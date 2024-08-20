from django.db import models

# Create your models here.

class student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=50)
    father_name=models.CharField( max_length=50)
    address=models.CharField( max_length=50)
    email=models.EmailField( max_length=70)

    def __str__(self):
        return str(self.stuname)

