from django import forms
from django.forms import ModelForm
from .models import RequestResponse,ResponseData,ResponseCategory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Div, HTML



class RequestResponseForm(forms.ModelForm):
	

	# def __init__(self, *args, **kwargs):
	# 	super(RequestResponseForm, self).__init__(*args, **kwargs)
	# 	self.helper = FormHelper()
	# 	self.helper.add_input(Submit('submit', 'Save Request', css_class='btn-primary float-right',style='width:200px;'))
	# 	self.helper.layout = Layout(Fieldset('',
	# 				HTML("""
	# 				<div class="container-fullwidth" style="background-color:#2d5d7b;margin-top:30px;margin-bottom-15px;color:white;">
	# 				<p style="padding:5px;padding-left:50px;">Personal Information</strong></p>
	# 				</div>
	# 				"""),
	# 				Div(
	# 				Div('request',css_class='col-xs-4 mr-4',style="width:250px"),
	# 				Div('company',css_class='col-xs-4 mr-4',style="width:250px"),
	# 				Div('response_file',css_class='col-xs-4 mr-4',style="width:250px"),
	# 				css_class='row',style='padding-left:200px'),
	# 				Div(
	# 				Div('sent',css_class='col-xs-4 mr-4',style="width:250px"),
	# 				Div('email',css_class='col-xs-4 mr-4',style="width:250px"),
	# 				css_class='row',style='padding-left:200px'),

	# 				)
	# 				)

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

	def __init__(self, *args, **kwargs):
		super(ResponseDataForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Save Request', css_class='btn-primary float-right',style='width:200px;margin-right:400px;'))
		self.helper.layout = Layout(Fieldset('',
					HTML("""
					<div class="container-fullwidth" style="background-color:#2d5d7b;margin-top:30px;margin-bottom-15px;color:white;">
					<p style="padding:5px;padding-left:50px;">Metadata</strong></p>
					</div>
					"""),
					Div(
					Div('request',css_class='col-xs-2 mr-4',style="width:250px"),
					Div('request_response',css_class='col-xs-2 mr-4',style="width:250px"),
					Div('metadata',css_class='col-xs-2 mr-4',style="width:250px"),
					Div('encrypted',css_class='col-xs-2',style="width:250px;margin-top:35px;"),
					Div('exclude_from_report',css_class='col-xs-2',style="width:250px;margin-top:35px;"),
					css_class='row',style='padding-left:200px'),
					HTML("""
					<div class="container-fullwidth" style="background-color:#2d5d7b;margin-top:30px;margin-bottom-15px;color:white;">
					<p style="padding:5px;padding-left:50px;">Data Value</strong></p>
					</div>
					"""),
					Div(
					Div('value',css_class='col-xs-6 mr-4'),
					Div('source_system',css_class='col-xs-6 mr-4'),
					
					css_class='row',style='padding-left:200px'),

					)
					)



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

class ResponseCategoryForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ResponseCategoryForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Save Request', css_class='btn-primary float-right',style='width:200px;margin-right:400px;'))
		self.helper.layout = Layout(Fieldset('',
					HTML("""
					<div class="container-fullwidth" style="background-color:#2d5d7b;margin-top:30px;margin-bottom-15px;color:white;">
					<p style="padding:5px;padding-left:50px;">Parent Records</strong></p>
					</div>
					"""),
					Div(
					Div('request',css_class='col-xs-2 mr-4',style="width:250px"),
					Div('request_response',css_class='col-xs-2 mr-4',style="width:250px"),
					css_class='row',style='padding-left:200px'),
					HTML("""
					<div class="container-fullwidth" style="background-color:#2d5d7b;margin-top:30px;margin-bottom-15px;color:white;">
					<p style="padding:5px;padding-left:50px;">Category</strong></p>
					</div>
					"""),
					Div(
					Div('data_category',css_class='col-xs-6 mr-4'),
					Div('exclude_from_report',css_class='col-xs-6 mr-4',style='margin-top:35px;'),
					
					css_class='row',style='padding-left:200px'),

					)
					)



	class Meta:
		model = ResponseCategory

		fields = [
			'request',
			'request_response',
			'data_category',
			'exclude_from_report',
			
		]