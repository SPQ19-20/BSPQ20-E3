from django import forms
from django.forms import CheckboxInput, HiddenInput

class NotificationsForm(forms.Form):
    active = forms.CharField(label='Your name', max_length=100)


class DarkmodeForm(forms.Form):
	active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'onchange': 'this.form.submit();'}))
	def __init__(self, checked, *args, **kwargs):
		super(DarkmodeForm, self).__init__(*args, **kwargs)
		if(checked == "True"):
			self.fields[active].widget = forms.CheckboxInput(attrs={'onchange': 'this.form.submit();', 'checked': ''})