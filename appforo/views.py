from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from appforo.forms import *
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView
from django.views import View
from django.contrib.auth.models import User
from django.core.mail import EmailMessage #Para poder enviar el mensaje

class foros(ListView):
    model=Foros
    template_name = 'index.html'

def respuestas(request, post_id):
    r=Respuestas.objects.filter(post=post_id)
    nomPost=Posts.objects.get(pk=post_id)
    usuario=Usuarios.objects.all()
    context = {'respuestas': r, 'nomPost': nomPost, 'usuario':usuario}
    if int(r.count())>0:
        return render(request, 'respuestas.html', context)
    else:
        return render(request, 'noRespuestas.html', context)

def registro(request):
    if request.method=='POST':
        form=usuarioForm(request.POST, request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            u_username=cd['username']
            u_email=cd['email']
            u_password=cd['password']
            u_nombre=cd['nombre']
            u_fechaNacimiento = cd['fechaNacimiento']
            u_imagen = cd['imagen']
            if(u_imagen == None):
                u_imagen='fotos/defecto.png'
            nuevo_user=User.objects.create_user(u_username, u_email, u_password)
            nuevo_user.save()
            u=User.objects.get(username=u_username)
            usuario=Usuarios(usuario=u, nombre=u_nombre, fechaNacimiento=u_fechaNacimiento, imagen=u_imagen)
            usuario.save()
            return HttpResponseRedirect("../")
    else:
        form=usuarioForm()
    return render(request, 'registro.html', {'form':form})

def posts(request, foro_id):
    p=Posts.objects.filter(foro=foro_id)
    nomForo=Foros.objects.get(pk=foro_id)
    context={'post':p, 'nomForo':nomForo}
    if int(p.count())>0:
        return render(request, 'posts.html', context)
    else:
        return render(request, 'noPosts.html', context)

class crearPost(View):
    def get(self, request, foro_id):
        form=PostForm()
        foro=Foros.objects.get(pk=foro_id)
        context= {'form': form, 'foro':foro}
        return render(request, 'crearPost.html', context)

    def post(self, request, foro_id):
        form=PostForm(request.POST)
        foro = Foros.objects.get(pk=foro_id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/foros/posts/"+str(foro_id))
        context = {'form': form, 'foro': foro}
        return render(request, 'crearPost.html', context)

class crearRespuesta(View):
    def get(self, request, post_id, user_id):
        form=RespuestaForm()
        post = Posts.objects.get(pk=post_id)
        usuarios = Usuarios.objects.all()
        u = User.objects.get(pk=user_id)

        idUsuario = 0
        for user in usuarios:
            if u.id == user.usuario.id:
                idUsuario = user.id

        context={'form':form, 'post':post, 'idUsuario':idUsuario}
        return render(request, 'crearRespuestas.html', context)

    def post(self, request, post_id, user_id):
        form=RespuestaForm(request.POST)
        post = Posts.objects.get(pk=post_id)
        usuarios=Usuarios.objects.all()
        u=User.objects.get(pk=user_id)

        idUsuario=0
        for user in usuarios:
            if u.id==user.usuario.id:
                idUsuario=user.id

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/foros/respuestas/"+str(post_id))
        context={'form':form, 'post':post, 'idUsuario':idUsuario}
        return render(request, 'crearRespuestas.html', context)

#Formulario de envio de mensaje
@login_required()
def contacto(request):
    if request.method=='POST':
        form=contactoForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            f_asunto=cd['asunto']
            f_mensaje=cd['mensaje']
            f_email=cd['correo']
            mail=EmailMessage(f_asunto, f_mensaje, f_email, to=['jose.django.cadiz@gmail.com'])
            mail.send()
            return HttpResponseRedirect('../')
    else:
        form=contactoForm()
    return render(request, 'contacto.html', {'form':form})

class normas(TemplateView):#Muestra un template sin datos
    template_name = 'normas.html'
