from django import forms
from django.forms import ModelForm
from response_metadata.models import Metadata,MetadataCategory

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

class MetadataCategoryForm(forms.ModelForm):

	class Meta:
		model = MetadataCategory

		fields = [
			'category',
			'consumer_label',
			'consumer_description',
			'sequence',
			'category_type',
			'company',
		]

