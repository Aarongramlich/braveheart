from django.db import models
from request_form_app.models import Request,Company

# Create your models here.



class Metadata(models.Model):
	
	data_category_choices = (
		('personal','Personal Information'),
		('commercial','Commercial Information'),
		('biometric','Biometric Information'),
		('internet','Internet Activity'),
		('geolocation', 'Geolocation Information'),
		('sensory','Sensory Information'),
		('psychometric','Psychometric Information'),
		('employment','Employment Information'),
		('inferred','Inferred Information'),
		)


	field	= models.TextField(max_length=255,blank=False) #stores the api name
	label	= models.TextField(max_length=255,blank=False) #stores the readable label of the field
	field_type = models.TextField(max_length=255,blank=True)
	consumer_label	= models.TextField(max_length=255,blank=False) #the label that will be used on consumer facing reports
	description = models.TextField(max_length=255,blank=True) #the label that will be used on consumer facing reports
	consumer_description = models.TextField(max_length=255,blank=True) #the field description that will be used on consumer facing reports
	data_category = models.TextField(max_length=255,choices=data_category_choices,blank=False)
	company		= models.ForeignKey(Company,on_delete=models.CASCADE,null=False,blank=False)
	created_at 	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.field + ' - ' + self.company.company_name