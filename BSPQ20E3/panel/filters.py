from .models import Entry, Data
import django_mongoengine_filter
from .cache import Cache
from django import forms

class DataFilter(django_mongoengine_filter.FilterSet):
	#https://pypi.org/project/django-mongoengine-filter/

	Country_Region = django_mongoengine_filter.ChoiceFilter(choices=Cache().COUNTRY_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
	Last_Update = django_mongoengine_filter.StringFilter()

	class Meta:
		model = Data
		fields = ['Country_Region', 'Last_Update']