from django.forms import ModelForm
from .models import Consumer

class ConsumerBasicInfoForm(ModelForm):
	class Meta:
		model = Consumer
		fields = ['first_name','last_name','email']

form = ConsumerBasicInfoForm()

