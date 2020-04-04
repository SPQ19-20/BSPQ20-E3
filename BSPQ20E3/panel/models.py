from django.db import models
from mongoengine import *

# Create your models here.
class Entry(Document):
	CCAA = StringField()
	Confirmados = IntField()
	Fecha = StringField() #Lo cambiaré a DataTimeField una vez tengamos los datos

class Data(Document):
	FIPS = IntField()
	Admin2 = StringField()
	Province_State = StringField()
	Country_Region = StringField()
	Last_Update = StringField()
	Lat = FloatField()
	Long_ = FloatField()
	Confirmed = IntField()
	Deaths = IntField()
	Recovered = IntField()
	Active = IntField()
	Combined_Key = StringField()
