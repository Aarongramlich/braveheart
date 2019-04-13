from django import forms
from django.forms import ModelForm
from .models import Consumer,Case
from localflavor.us.models import USStateField, USSocialSecurityNumberField, USZipCodeField



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

class CaseForm(forms.ModelForm):
	
	class Meta:
		model = Case
		fields = ['first_name','last_name','email','alternative_email', 'primary_address', 'primary_address_line_two','primary_city','primary_state','primary_zip','primary_country','delete_request','what_request','who_request','opt_out_request']

		labels = {
			'primary_address' : 'Address',
			'primary_address_line_two' : 'Address 2',
			'primary_city' : 'City',
			'primary_state' : 'State',
			'primary_zip' : 'Zip',
			'delete_request':'Delete all of my applicable data',
			'what_request': 'Learn more about what data we store',
			'who_request': 'Find out who we share data with',
			'opt_out_request':'Opt-out of the future sharing of my data',
		}

	

	# form = ConsumerBasicInfoForm(request.POST)
	# new_consumer = form.save()
