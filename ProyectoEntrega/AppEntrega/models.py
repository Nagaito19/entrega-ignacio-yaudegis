from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

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

class Avatar(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to="avatares", null=True,blank=True)

    def __str__(self) -> str:
        return self.user.username


class post(models.Model):
    id=models.AutoField(primary_key= True)
    titulo = models.CharField('Titulo', max_length=90, blank=False, null= False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    description = models.CharField('descripcion', max_length=110, blank=False, null= False)
    contenido=RichTextField()
    imagen = models.URLField(max_length=255, blank=False, null=False)
    autor = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    #categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name='POST'
        verbose_name_plural= 'POST'

    def __str__(self):
        return self.titulo 

