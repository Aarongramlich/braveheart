from django import forms
from django.forms import ModelForm
from request_form_app.models import Consumer,Request,Company
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Div, HTML



class RequestForm(forms.ModelForm):
	

	def __init__(self, *args, **kwargs):
		super(RequestForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Save Request', css_class='btn-primary float-right',style='width:200px;'))
		self.helper.layout = Layout(Fieldset('',
					HTML("""
					<div class="container-fullwidth" style="background-color:#2d5d7b;margin-top:30px;margin-bottom-15px;color:white;">
					<p style="padding:5px;padding-left:50px;">Personal Information</strong></p>
					</div>
					"""),
					Div(
					Div('first_name',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('last_name',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('email',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('alternative_email',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('consumer',css_class='col-xs-4 mr-4',style="width:250px"),
					css_class='row',style='padding-left:200px'),
					Div(
					Div('phone',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('alternative_phone',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('ssn',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('date_of_birth',css_class='col-xs-4 mr-4',style="width:250px"),
					css_class='row',style='padding-left:200px'),
					HTML("""
					<div class="container-fullwidth" style="background-color:#2d5d7b;margin-top:30px;margin-bottom-15px;color:white;">
					<p style="padding:5px;padding-left:50px;">General Request Information</strong></p>
					</div>
					"""),
					Div(
					Div('company_requested',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('request_source',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('website_source',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('terms_of_service_signed',css_class='col-xs-4 mr-4',style='margin-top:35px; width:250px'),
					Div('data_ready_to_send',css_class='col-xs-4 mr-4',style="width:250px"),
					css_class='row',style='padding-left:200px'),
					
					HTML("""
					<div class="container-fullwidth" style="background-color:#2d5d7b;margin-top:30px;margin-bottom-15px;color:white;">
					<p style="padding:5px;padding-left:50px;">Address Information</strong></p>
					</div>
					"""),
					Div(
					Div('primary_address',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('primary_address_line_two',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('primary_city',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('primary_state',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('primary_zip',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('primary_country',css_class='col-xs-4 mr-4',style="width:250px"),
					css_class='row',style='padding-left:200px'),
					Div(
					Div('alternative_address',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('alternative_address_line_two',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('alternative_city',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('alternative_state',css_class='col-xs-4 mr-4',style="width:250px"),
					# Div('alternative_zip',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('alternative_country',css_class='col-xs-4 mr-4',style="width:250px"),
					css_class='row',style='padding-left:200px'),
					HTML("""
					<div class="container-fullwidth" style="background-color:#2d5d7b;margin-top:30px;margin-bottom-15px;color:white;">
					<p style="padding:5px;padding-left:50px;">Request Type</strong></p>
					</div>
					"""),
					Div(
					Div('who_request',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('opt_out_request',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('delete_request',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('priority',css_class='col-xs-4 mr-4',style="width:250px"),
					css_class='row',style='padding-left:200px'),

				)
				)

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
			'company_code',
			'website',
			'primary_contact',
			'address',
			'address_line_two',
			'city',
			'state',
			'zip_code',
			'country',
			'logo',


		]

class ConsumerForm(forms.ModelForm):


	def __init__(self, *args, **kwargs):
		super(ConsumerForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Save Request', css_class='btn-primary float-right',style='width:200px;'))
		self.helper.layout = Layout(Fieldset('',
					HTML("""
					<div class="container-fullwidth" style="background-color:#2d5d7b;margin-top:30px;margin-bottom-15px;color:white;">
					<p style="padding:5px;padding-left:50px;">Personal Information</strong></p>
					</div>
					"""),
					Div(
					Div('first_name',css_class='col-xs-3 mr-4',style="width:250px"),
					Div('last_name',css_class='col-xs-3 mr-4',style="width:250px"),
					Div('email',css_class='col-xs-3 mr-4',style="width:250px"),
					Div('alternative_email',css_class='col-xs-4 mr-4',style="width:250px"),
					css_class='row',style='padding-left:200px'),
					Div(
					Div('phone',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('alternative_phone',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('ssn',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('date_of_birth',css_class='col-xs-4 mr-4',style="width:250px"),
					css_class='row',style='padding-left:200px'),
					Div(
					Div('driver_license_state',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('driver_license_number',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('identity_verified',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('terms_of_service_signed',css_class='col-xs-4 mr-4',style="width:250px;margin-top:30px;"),
					css_class='row',style='padding-left:200px'),
					
					
					HTML("""
					<div class="container-fullwidth" style="background-color:#2d5d7b;margin-top:30px;margin-bottom-15px;color:white;">
					<p style="padding:5px;padding-left:50px;">Address Information</strong></p>
					</div>
					"""),
					Div(
					Div('primary_address',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('primary_address_line_two',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('primary_city',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('primary_state',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('primary_zip',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('primary_country',css_class='col-xs-4 mr-4',style="width:250px"),
					css_class='row',style='padding-left:200px'),
					Div(
					Div('alternative_address',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('alternative_address_line_two',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('alternative_city',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('alternative_state',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('alternative_zip',css_class='col-xs-4 mr-4',style="width:250px"),
					Div('alternative_country',css_class='col-xs-4 mr-4',style="width:250px"),
					css_class='row',style='padding-left:200px'),
					

				)
				)



	class Meta:
		model = Consumer

		fields = [
			'first_name',
			'last_name',
			'email',
			'alternative_email',
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
			'alternative_zip',
			'alternative_country',
			'ssn',
			'driver_license_number',
			'driver_license_state',
			'date_of_birth',
			'terms_of_service_signed',
			'identity_verified',
			'phone',
			'alternative_phone',
			]
