from .models import Entry, Data
import django_mongoengine_filter
from .cache import Cache
from django import forms
from mongoengine import *


class DataFilter(django_mongoengine_filter.FilterSet):
	#https://pypi.org/project/django-mongoengine-filter/

	Country_Region = django_mongoengine_filter.ChoiceFilter(choices=Cache().COUNTRY_CHOICES, widget=forms.Select(attrs={'onchange': 'this.form.submit();', 'class': 'selectpicker', 'data-live-search': 'true'}))
	Last_Update = django_mongoengine_filter.ChoiceFilter(choices=Cache().DATE_CHOICES, widget=forms.Select(attrs={'onchange': 'this.form.submit();', 'class': 'selectpicker', 'data-live-search': 'true'}))

	class Meta:
		model = Data
		fields = ['Country_Region', 'Last_Update']

		"""filter_overrides = {
			StringField: {
				'filter_class': django_mongoengine_filter.ChoiceFilter,
				'extra': lambda f: {
					'lookup_expr': 'icontains',
					'widget': forms.Select(attrs={'onchange': 'this.form.submit();', 'class': 'selectpicker', 'data-live-search': 'true'}),
				},
			},
		}"""