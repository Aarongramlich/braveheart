from django import forms
from django.forms import ModelForm
from .models import RequestResponse,ResponseData




class RequestResponseForm(forms.ModelForm):
	class Meta:
		model = RequestResponse

		fields = [
			'request',
			'company',
			'response_file',
			'sent',
			'email'
		]


class ResponseDataForm(forms.ModelForm):
	class Meta:
		model = ResponseData

		fields = [
			'request',
			'request_response',
			'metadata',
			'value',
			'encrypted',
			'exclude_from_report',
			'source_system',
		]