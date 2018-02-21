"""foro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appforo import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('iniciarSesion/', login,{'template_name':'login.html'}, name="login"),
    path('cierreSesion/', logout,{'template_name':'logout.html'}, name="logout"),
    path('', views.foros.as_view(), name='foros'),
    path('registro/', views.registro, name='registro'),
    path('posts/<int:foro_id>', views.posts, name="posts"),
    path('posts/crearPost/<int:foro_id>', views.crearPost.as_view(), name="crearPost"),
    path('respuestas/<int:post_id>', views.respuestas, name="respuestas"),
    path('respuestas/crearRespuestas/<int:post_id><int:user_id>', views.crearRespuesta.as_view(), name="crearRespuesta"),
    path('contacto/', views.contacto, name='contacto'),
    path('normas/', views.normas.as_view(), name='normas'),
]