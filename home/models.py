from django.db import models

# Create your models here.
class Login(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    contact= models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name
    