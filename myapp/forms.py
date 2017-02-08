from __future__ import unicode_literals

from django import forms
from datetime import datetime

class ContactForm(forms.Form):
	
	subject = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control theme', 'required': 'True', 'help_text': '100 characters max.'}))
	sender = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'contact-form'}))
	message = forms.CharField(max_length=1000)