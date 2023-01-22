"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import *

from django.urls import path , include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('home/', login_required( Home.as_view() ) , name='home'),
    path('descarga_xml/', login_required( Descargar_XML.as_view() ) , name="descarga_xml"),
    path('obtener_xml/', login_required( Obtener_XML.as_view() ) , name="obtener_xml_user" ),
    path('descarga_xml_file/<int:id_xml>', login_required( descargar_xml_file ) , name="obtener_xml_descargado" ),
    path('borrar_xml_file/', login_required( borrar_xml_file ) , name="borrar_xml_file" ),
    
    
]
