from .models import Entry, Data
import django_mongoengine_filter

class DataFilter(django_mongoengine_filter.FilterSet):
	#https://pypi.org/project/django-mongoengine-filter/
	#COUNTRIES = Data.objects.values_list('Country_Region')
	Country_Region = django_mongoengine_filter.StringFilter()
	Last_Update = django_mongoengine_filter.StringFilter()

	class Meta:
		model = Data
		fields = ['Country_Region', 'Last_Update']