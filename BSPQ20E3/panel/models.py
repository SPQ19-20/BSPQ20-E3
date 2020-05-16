from django.db import models
from mongoengine import *
from .cache import Cache

"""
MongoDB "Schema".
"""
# Create your models here.
class Entry(Document):
    """
    A class used to represent an Entry

    """
    CCAA = StringField()
    Confirmados = IntField(localize=True)
    Fecha = StringField() #Lo cambiaré a DataTimeField una vez tengamos los datos

class Data(Document):
	"""
    A class used to represent each data entry (with more information)

    """
	FIPS = IntField(localize=True)
	Admin2 = StringField()
	Province_State = StringField()
	Country_Region = StringField()
	Last_Update = StringField()
	Lat = FloatField(localize=True)
	Long_ = FloatField(localize=True)
	Confirmed = IntField(localize=True)
	Deaths = IntField(localize=True)
	Recovered = IntField(localize=True)
	Active = IntField(localize=True)
	Combined_Key = StringField()


class Auth_user(Document):
    """"
    A class used to represent each user

    """
    password = StringField()
    last_login = StringField()
    is_superuser = StringField()
    username = StringField()
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    is_staff = StringField()
    is_active = BooleanField()
    date_joined = StringField()
