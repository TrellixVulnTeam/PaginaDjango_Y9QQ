from django.db import models
from django.contrib.auth.models import User

class Foros(models.Model):
    nombre=models.CharField(max_length=30, null=False, unique=True)
    descripcion=models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.nombre

class Posts(models.Model):
    titulo=models.CharField(max_length=80, null=False)
    foro=models.ForeignKey(Foros, on_delete=models.CASCADE)
    fechaPublicacion=models.DateField(auto_now=True)
    def __str__(self):
        return self.titulo

class Usuarios(models.Model):
    usuario=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=10, null=False)
    fechaNacimiento=models.DateField(null=False)
    imagen=models.ImageField(upload_to="fotos/", blank=True, default='fotos/defecto.png')
    fechaRegistro=models.DateField(auto_now=True)
    def __str__(self):
        return self.nombre

class Respuestas(models.Model):
    respuesta=models.CharField(max_length=200)
    fechaPublicacion = models.DateField(auto_now=True)
    usuario=models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    post=models.ForeignKey(Posts, on_delete=models.CASCADE)
    def __str__(self):
        return self.respuesta
