from django.contrib import admin
from appforo.models import *
from django import forms

class UsuariosAdmin(admin.ModelAdmin):
    list_per_page = 10
    actions_on_top = False
    actions_on_bottom = True
    ordering = ['nombre']
    search_fields = ['fechaNacimiento', 'fechaRegistro']

class ForosAdminForm(forms.ModelForm):
    def clean_nombre(self):
        nombre=self.cleaned_data['nombre']
        if len(nombre)<2:
            raise forms.ValidationError("Nombre demasiado corto")
        elif nombre.count("@")>0 or nombre.count("'")>0 or nombre.count(".")>0 or nombre.count(";")>0:
            raise forms.ValidationError("El nombre del foro no puede contener caracteres especiales")
        else:
            return self.cleaned_data['nombre']

class ForosAdmin(admin.ModelAdmin):
    form=ForosAdminForm

class PostInline(admin.StackedInline):
    model=Posts

# Register your models here.
admin.site.register(Foros, ForosAdmin)
admin.site.register(Posts)
admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Respuestas)