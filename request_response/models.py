from django.db import models
from request_form_app.models import Request,Company
from response_metadata.models import Metadata,MetadataCategory
from django.urls import reverse,reverse_lazy


# Create your models here.

class RequestResponse(models.Model):

	request 	= models.ForeignKey(Request,on_delete=models.CASCADE,blank=False)
	company 	= models.ForeignKey(Company,on_delete=models.CASCADE,blank=True)
	response_file = models.FileField(upload_to='request_response',blank=True)
	created_at	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)
	sent = models.BooleanField(default=False)
	sent_date_time = models.DateTimeField(blank=True,null=True)
	email = models.EmailField(blank=True,null=True)

	def __str__(self):
		return self.request.email + ' - ' + self.request.company_requested.company_name

	def get_absolute_url(self):
		return reverse('user_console:request_detail',kwargs={'pk':self.request.pk})



	# def get_absolute_url(self):
	# 	return reverse("user_console:request_detail",kwargs={'pk',self.request.pk})

class ResponseData(models.Model): #WILL BE USED FOR API/JSON INSERTS "DAY 2"

	request		= models.ForeignKey(Request,on_delete=models.CASCADE,blank=False)
	request_response = models.ForeignKey(RequestResponse,on_delete=models.CASCADE,blank=False)
	metadata	= models.ForeignKey(Metadata,on_delete=models.CASCADE,blank=False)
	value 		= models.TextField(max_length=255,blank=True,null=True)
	encrypted 	= models.BooleanField(default=False)
	exclude_from_report = models.BooleanField(default=False)
	source_system = models.TextField(max_length=255,blank=True,null=True)
	created_at 	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.metadata.field + ' - ' + self.value + ' - ' + self.request.email

	def get_absolute_url(self):
		return reverse('user_console:request_detail',kwargs={'pk':self.request.pk})

class ResponseCategory(models.Model):

	request = models.ForeignKey(Request,on_delete=models.CASCADE,blank=False)
	request_response = models.ForeignKey(RequestResponse,on_delete=models.CASCADE,blank=False)
	data_category	= models.ForeignKey(MetadataCategory,on_delete=models.CASCADE,blank=False)
	exclude_from_report = models.BooleanField(default=False)
	created_at 	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.data_category.category + ' - ' + self.request.email