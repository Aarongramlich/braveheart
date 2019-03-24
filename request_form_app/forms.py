from django import forms
from django.forms import ModelForm
from .models import Consumer

# form = ConsumerBasicInfoForm()

class ConsumerBasicInfoForm(forms.ModelForm):
	class Meta:
		model = Consumer
		fields = ['first_name','last_name','email']

		widgets = {
				'first_name' : forms.TextInput (
				attrs={'placeholder':'First Name'}				
					)			
		}



