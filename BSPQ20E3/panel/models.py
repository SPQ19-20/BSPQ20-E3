from django.db import models
from mongoengine import *
"""
MongoDB "Schema".
"""
# Create your models here.
class Entry(Document):
    """
    A class used to represent an Entry

    ...

    Attributes
    ----------
    CCAA : str
        a formatted string to store the CCAA
    Confirmados : int
        a formatted integer to store the number of confirmed cases
    Fecha : str
        a formatted string to store the Date
    """
    CCAA = StringField()
    Confirmados = IntField(localize=True)
    Fecha = StringField() #Lo cambiaré a DataTimeField una vez tengamos los datos

class Data(Document):
	"""
    A class used to represent each data entry (with more information)

    ...

    Attributes
    ----------
    FIPS : int
        a formatted integer to store the Federal Information Processing Standard
    Admin2 : str
        a formatted string to store the county
    Province_State : str
        a formatted string to store the Province/State
    CountryRegion : str
        a formatted string to store the CountryRegion
    Last_Update : str
        a formatted string to store the Date
    Lat : float
        a formatted float to store the Latitude
    Long_ : float
        a formatted float to store the Longitude
    Confirmed : int
        a formatted integer to store the number of confirmed cases
    Deaths : int
        a formatted integer to store the number of deaths
    Recovered : int
        a formatted integer to store the number of recovered cases
    Active: int
    	a formatted integer to store the status of the entry
    Combined_Key: str
    	a formatted string that helps grouping the information
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
    #id = IntField()
    password = StringField()
    last_login = StringField()
    is_superuser = StringField()
    username = StringField()
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    is_staff = StringField()
    is_active = StringField()
    date_joined = StringField()
