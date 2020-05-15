from django import forms
from django.forms import CheckboxInput, HiddenInput

class NotificationsForm(forms.Form):
	'''Creates the form

	:param req: Serialized JSON
	:type amount: Serialized JSON

	:returns: Defined by forms.Form
	:rtype: Defined by forms.Form

	This class is not used due to the existing problems 
	for editing data in the database (obsolete or unsupported libraries)
	'''
	active = forms.CharField(label='Your name', max_length=100)