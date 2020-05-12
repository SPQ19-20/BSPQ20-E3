from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponse
from .models import Entry, Data, Auth_user
from .cache import Cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import DataFilter
import os
import time
import datetime
# i18n
from django.utils import translation
from .forms import NotificationsForm, DarkmodeForm
# Create your views here.

def checkDarkMode(req):
	if req.method == 'POST':
		form = NotificationsForm(req.POST)
		if form.is_valid():
			print("HAY DARK")
			print("HAY DARK")
			print("HAY DARK")
			print("HAY DARK")
			if form.cleaned_data["active"] == "on":
				req.session['darkmode'] = "True"
			else:
				req.session['darkmode'] = "False"
			print(form.cleaned_data, "///////", req.session['darkmode'])
	if not 'darkmode' in req.session:
		req.session['darkmode'] = "False"

def checkPOST(req):
	"""
	hypothetically, the user's choice regarding receiving emails is returned in the form. 
	Instead, the library fails and does not perform the update correctly.

	if req.method == 'POST':
		form = NotificationsForm(req.POST) 
		if form.is_valid() and req.user.is_authenticated: 
			user = Auth_user.objects.filter(username=req.user.username).first()
			user.is_active = "true"
			user.save()
			return True 
	"""
	return False

def index(req):
	'''Loads the Main Page

	:param req: The Http Request
	:type amount: Http Request

	:returns: Http Response
	:rtype: Http
	'''
	#checkPOST(req)
	form = NotificationsForm();

	#Darkmode in session
	checkDarkMode(req)
	formDark = DarkmodeForm(req.session['darkmode']);

	if translation.LANGUAGE_SESSION_KEY in req.session: 
		del req.session[translation.LANGUAGE_SESSION_KEY]

	#Test para ver si inserta bien los datos
	#entry = Entry(CCAA="ComPrueba",Confirmados=999, Fecha= "1-1-1991")
	#entry.save()
	#dummy = Data(FIPS=0,Admin2="prueba")
	#dummy.save()
	prueba = Data.objects()

	return render(req, 'index.html', {'data' : prueba, 'form' : form, 'formDark' : formDark, 'darkmode' : req.session['darkmode']})

def livelog(req):
	dataFilter = DataFilter(req.GET, queryset=Data.objects())
	#dataFilter = ""
	#print(Cache().COUNTRIES)
	paginator = Paginator(dataFilter.qs[:10000], 25)
	
	'''Loads the Livelog

	:param req: The Http Request
	:type amount: Http Request

	:returns: Http Response
	:rtype: Http
	''' 

	page = req.GET.get('page', 1)
	index = int(page)
	max_index = len(paginator.page_range)
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index
	page_range = list(paginator.page_range)[start_index:end_index]

	try: data = paginator.page(page) 
	except PageNotAnInteger: 
		data = paginator.page(1) 
	except EmptyPage: 
		data = paginator.page(paginator.num_pages)
		
	return render(req, 'livelogtest.html', { 'filter' : dataFilter, 'data' : data, 'page_range': page_range, 'max_index': max_index})
