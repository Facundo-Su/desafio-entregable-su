from xml.dom.expatbuilder import DOCUMENT_NODE
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from aplicacion.models import Familiares
from django.template import loader
# Create your views here.

def familiares(request):
    familiar = Familiares.objects.all()
    return HttpResponse(familiar)

def altaDeFamiliar(request, nombre,dni,fechaDeNacimiento):
    familiar = Familiares(nombre =nombre , dni = dni, fechaDeNacimiento = fechaDeNacimiento)
    familiar.save()
    plantilla = loader.get_template("paginaExitosa.html")
    diccionario ={"nombre":nombre,"dni":dni,"fechaDeNacimiento":fechaDeNacimiento}
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def plantillaPrincipal (request):
    familiares = Familiares.objects.all()
    plantilla=loader.get_template("template.html")
    diccionario = {"familiares":familiares}
    documento =plantilla.render(diccionario)
    
    return HttpResponse(documento)