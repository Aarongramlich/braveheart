from django import forms
from django.forms import ModelForm
from .models import RequestResponse




class RequestResponseForm(forms.ModelForm):
	class Meta:
		model = RequestResponse

		fields = [
			'request',
			'company',
			'response_file',
		]