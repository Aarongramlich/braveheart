from django import forms
from django.forms import ModelForm
from .models import Consumer,Request
from localflavor.us.models import USStateField, USSocialSecurityNumberField, USZipCodeField
from django.core.mail import send_mail


class ConsumerForm(forms.ModelForm):

	primary_state = USStateField()
	primary_zip = USZipCodeField()
	ssn = USSocialSecurityNumberField()

	class Meta:
		model = Consumer
		fields = ['first_name','last_name','email','alternative_email', 'primary_address', 'primary_address_line_two','primary_city','primary_state','primary_zip','primary_country']

		labels = {
			'primary_address' : 'Address',
			'primary_address_line_two' : 'Address 2',
			'primary_city' : 'City',
			'primary_state' : 'State',
			'primary_zip' : 'Zip',
		}
		widgets = {
				'first_name' : forms.TextInput (
				attrs={'placeholder':'First Name'}				
					)

		}

class RequestForm(forms.ModelForm):
	
	class Meta:
		model = Request
		fields = ['first_name','last_name','email','alternative_email', 'primary_address', 'primary_address_line_two','primary_city','primary_state','primary_zip','primary_country','delete_request','what_request','who_request','opt_out_request']

		labels = {
			'primary_address' : 'Address',
			'primary_address_line_two' : 'Address 2',
			'primary_city' : 'City',
			'primary_state' : 'State',
			'primary_zip' : 'Zip',
			'delete_request':'Delete my data',
			'what_request': 'Find out what data we store',
			'who_request': 'Find out who we share with',
			'opt_out_request':'Opt-out of sharing my data',
		}

	# def send_email(self):
	# 	send_mail('Hello from Braveheart Data!',
	# 		'This is the automated message. <br> This is a test message',
	# 		'support@braveheartdata.com',
	# 		[Case.email],
	# 		fail_silently=False)
	

	# form = ConsumerBasicInfoForm(request.POST)
	# new_consumer = form.save()
