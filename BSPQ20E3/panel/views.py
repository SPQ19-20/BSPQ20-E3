from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponse
from .models import Entry, Data
import os
import time
import datetime





# Create your views here.
def index(req):
	#Test para ver si inserta bien los datos
	#entry = Entry(CCAA="ComPrueba",Confirmados=999, Fecha= "1-1-1991")
	#entry.save()
	#dummy = Data(FIPS=0,Admin2="prueba")
	#dummy.save()
	prueba = Data.objects()

	return render(req, 'index.html', {'data' : prueba})

def settings(req):
	return render(req, 'settings.html', {
    })