from django.db import models
from mongoengine import *

# Create your models here.
class Entry(Document):
	CCAA = StringField()
	Confirmados = IntField()
	Fecha = StringField() #Lo cambiaré a DataTimeField una vez tengamos los datos