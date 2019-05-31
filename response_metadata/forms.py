from django import forms
from django.forms import ModelForm
from response_metadata.models import Metadata

class MetadataForm(forms.ModelForm):
	class Meta:
		model = Metadata

		fields = [
			'field',
			'label',
			'field_type',
			'consumer_label',
			'description',
			'consumer_description',
			'data_category',
			'company',
			'sequence',
		]