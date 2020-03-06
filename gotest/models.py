from django.db import models

# Create your models here.


class Essay2(models.Model):
       
    q1  =models.CharField(max_length=150)
    q2  =models.CharField(max_length=150)
    q3  =models.CharField(max_length=150)
    q4  =models.CharField(max_length=150)
    q5  =models.CharField(max_length=150)
    q6  =models.CharField(max_length=150)
    q7  =models.CharField(max_length=150)
    q8  =models.CharField(max_length=150)
    q9  =models.CharField(max_length=150)
    q10  =models.CharField(max_length=150)
    
    
    def __str__(self):
        return self.name