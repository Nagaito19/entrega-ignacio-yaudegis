from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    def __str__(self):
        return self.nombre + " " + self.apellido+ " " + self.email

class Truco(models.Model):
    nombre= models.CharField(max_length=40)
    clase= models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + '' + self.clase 

class Mago(models.Model):
    nombre= models.CharField(max_length=40) 
    apellido= models.CharField(max_length=40)
    def __str__(self):
        return self.nombre + " " + self.apellido
        
class Estilo(models.Model):
    nombre= models.CharField(max_length=40) 
    def __str__(self):
        return self.nombre 

class avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to="avatares", null=True,blank=True)

    def __str__(self) -> str:
        return self.user.username
