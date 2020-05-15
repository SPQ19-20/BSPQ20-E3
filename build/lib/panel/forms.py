from django import forms
from django.forms import CheckboxInput, HiddenInput

class NotificationsForm(forms.Form):
    active = forms.CharField(label='Your name', max_length=100)