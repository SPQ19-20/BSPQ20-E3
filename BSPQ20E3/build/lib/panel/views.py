from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponse
from .models import Entry, Data
import os
import time
import datetime
# i18n
from django.utils import translation

# Create your views here.
def index(req):
	'''Loads the Main Page

        :param req: The Http Request
        :type amount: Http Request

        :returns: Http Response
        :rtype: Http
    '''
	if translation.LANGUAGE_SESSION_KEY in req.session: 
		del req.session[translation.LANGUAGE_SESSION_KEY]
	#Test para ver si inserta bien los datos
	#entry = Entry(CCAA="ComPrueba",Confirmados=999, Fecha= "1-1-1991")
	#entry.save()
	#dummy = Data(FIPS=0,Admin2="prueba")
	#dummy.save()
	prueba = Data.objects()

	return render(req, 'index.html', {'data' : prueba})

def settings(req):
	if translation.LANGUAGE_SESSION_KEY in req.session: 
		del req.session[translation.LANGUAGE_SESSION_KEY]

	return render(req, 'settings.html', { })

def livelog(req):
	'''Loads the Livelog

        :param req: The Http Request
        :type amount: Http Request

        :returns: Http Response
        :rtype: Http
    ''' 
	if translation.LANGUAGE_SESSION_KEY in req.session: 
		del req.session[translation.LANGUAGE_SESSION_KEY]

	prueba = Data.objects()[:10000]
	return render(req, 'livelogtest.html', { 'data' : prueba })


