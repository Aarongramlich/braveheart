from django import forms
from django.forms import ModelForm
from .models import Consumer
from localflavor.us.models import USStateField, USSocialSecurityNumberField, USZipCodeField


# form = ConsumerBasicInfoForm()

class ConsumerBasicInfoForm(forms.ModelForm):
	
	primary_state = USStateField()
	primary_zip = USZipCodeField()
	ssn = USSocialSecurityNumberField()
	class Meta:
		model = Consumer
		fields = ['first_name','last_name','email','alternative_email', 'primary_address', 'primary_address_line_two','primary_city','primary_state','primary_zip','primary_country']

		labels = {
			'primary_address' : 'Priamry Address',
			'primary_address_line_two' : 'Primary Address 2',
			'primary_city' : 'City',
			'primary_state' : 'State',
			'primary_zip' : 'Zip',
		}
		widgets = {
				'first_name' : forms.TextInput (
				attrs={'placeholder':'First Name'}				
					)

		}