from __future__ import unicode_literals

from django import forms
from datetime import datetime

class ContactForm(forms.Form):
	
	subject = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control theme', 'required': 'True'}))
	sender = forms.EmailField(max_length=254)
	message = forms.CharField(max_length=1000)