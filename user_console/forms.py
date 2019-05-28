from django import forms
from django.forms import ModelForm
from request_form_app.models import Consumer,Request,Company


class RequestForm(forms.ModelForm):
	class Meta:
		model = Request

		fields = ['consumer',
		'company_requested',
		'request_source',
		'website_source',
		'what_request',
		'who_request',
		'opt_out_request',
		'delete_request',
		'priority',
		'escalated',
		'stage',
		'first_name',
		'last_name',
		'email',
		'alternative_email',
		'phone',
		'alternative_phone',
		'primary_address',
		'primary_address_line_two',
		'primary_city',
		'primary_state',
		'primary_zip',
		'primary_country',
		'alternative_address',
		'alternative_address_line_two',
		'alternative_city',
		'alternative_state',
		'alternative_country',
		'ssn',
		'driver_license_number',
		'driver_license_state',
		'date_of_birth',
		'terms_of_service_signed',
		'data_ready_to_send',
		'status',
		'days_open',
		
		]

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company

		fields = [
			'company_name',
			'website',
			'primary_contact'
		]

class ConsumerForm(forms.ModelForm):
	class Meta:
		model = Consumer

		fields = [
			'first_name',
			'last_name',
			'email',
		]
