from django import forms
from django.forms import ModelForm
from appforo.models import Usuarios
from appforo.models import Respuestas
from appforo.models import Posts
from appforo.models import Foros
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
import time

class usuarioForm(forms.Form):
    username=forms.CharField(max_length=15, label="Nombre de usuario")
    email=forms.EmailField(max_length=30, label="Email")
    password=forms.CharField(max_length=10, widget=forms.PasswordInput)
    nombre=forms.CharField(max_length=10, label="Nombre personal")
    fechaNacimiento=forms.DateField(label="Fecha de nacimiento (año-mes-dia)")
    imagen=forms.ImageField(widget=forms.FileInput, required=False)
    captcha=CaptchaField()

    def clean_username(self):
        usuario=User.objects.all()
        for user in usuario:
            if user.username == self.cleaned_data['username']:
                raise forms.ValidationError("El nombre de usuario ya existe, por favor seleccione otro.")
        return self.cleaned_data['username']

    def clean_fechaNacimiento(self):
        x= str(self.cleaned_data['fechaNacimiento']).split("-")
        if int(x[0])<1930 or int(x[0])>int(time.strftime('%Y')):
            raise forms.ValidationError("Año incorrecto")
        elif int(x[1])<1 or int(x[1])>12:
            print(x[1])
            raise forms.ValidationError("Mes incorrecto")
        elif int(x[2])<1 or int(x[2])>31:
            raise forms.ValidationError("Dia incorrecto")
        return self.cleaned_data['fechaNacimiento']

    def clean(self):
        cleaned_data=self.cleaned_data
        return cleaned_data

class RespuestaForm(forms.ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=Respuestas
        fields=['post', 'usuario', 'respuesta']
        help_texts={
            'respuesta': ('Maximo de caracteres: 200')
        }
        widgets={
            'respuesta':forms.Textarea(),
            'post': forms.HiddenInput(),
            'usuario': forms.HiddenInput(),
        }


class PostForm(forms.ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=Posts
        fields=['foro','titulo']
        help_texts={
            'titulo': ('Titulo descriptivo del post')
        }
        widgets={
            'foro':forms.HiddenInput(),
        }
    def clean_titulo(self):
        if len(self.cleaned_data['titulo'])<5:
            raise forms.ValidationError("El nombre del post tiene que superar 5 caracteres, debe de ser un nombre descriptivo")
        return self.cleaned_data['titulo']


class contactoForm(forms.Form):
    asunto=forms.CharField(max_length=20)
    correo=forms.EmailField()
    mensaje=forms.CharField(max_length=200, widget=forms.Textarea)


