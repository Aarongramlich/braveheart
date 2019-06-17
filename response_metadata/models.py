from django.db import models
from request_form_app.models import Request,Company

# Create your models here.

class MetadataCategory(models.Model):

	category_type_choices = (
		('source','Data Source'),
		('vendor','3rd Party'),
		('data','Data')
		)


	category = models.TextField(max_length=255,blank=False,null=False)
	consumer_label = models.TextField(max_length=255,blank=False,null=False)
	consumer_description = models.TextField(max_length=255,blank=True)
	sequence = models.IntegerField(blank=True,default="1")
	created_at 	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)
	company		= models.ForeignKey(Company,on_delete=models.CASCADE,null=False,blank=False)
	category_type = models.TextField(max_length=255,choices=category_type_choices,blank=False,default='data')

	def __str__(self):
		return self.category + ' - ' + self.company.company_name

	def get_absolute_url(self):
		return revere("response_metadata:metadata_category_detail",kwargs={'pk':self.pk})

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

	metadata_key = models.TextField(max_length=255,blank=True,primary_key=True)
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
	sequence = models.IntegerField(blank=True,default="1")

	def __str__(self):
		return self.field + ' - ' + self.company.company_name

	def get_absolute_url(self):
		return revere("response_metadata:metadata_detail",kwargs={'pk':self.pk})

	def save(self,*args,**kwargs):

		self.metadata_key = self.field  + "_" + self.company.company_code
		# self.metadata_key.save()
		super(Metadata,self).save(*args,**kwargs)
