from django.db import models
from request_form_app.models import Request,Company
from response_metadata.models import Metadata
from django.urls import reverse,reverse_lazy


# Create your models here.

class RequestResponse(models.Model):

	request 	= models.ForeignKey(Request,on_delete=models.CASCADE,blank=True)
	company 	= models.ForeignKey(Company,on_delete=models.CASCADE,blank=True)
	response_file = models.FileField(upload_to='request_response')
	created_at	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)

	# def __str__(self):
	# 	return self.request

	def get_absolute_url(self):
		return reverse('request_response:response_detail',kwargs={'pk',self.pk})

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