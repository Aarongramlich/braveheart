from django.db import models
from request_form_app.models import Request,Company


# Create your models here.

class RequestResponse(models.Model):

	request 	= models.ForeignKey(Request,on_delete=models.CASCADE,blank=False)
	company 	= models.ForeignKey(Company,on_delete=models.CASCADE,blank=False)
	response_file = models.FileField(upload_to='request_response')
	created_at	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)

# class ResponseData(models.Model): #WILL BE USED FOR API/JSON INSERTS "DAY 2"

# 	request		= models.ForeignKey(Request,on_delete=models.CASCADE,blank=False)
# 	request_response = models.ForeignKey(RequestResponse,on_delete=models.CASCADE,blank=False)
# 	metadata	= models.ForeignKey(Metadata,on_delete=models.CASCADE,blank=False)
# 	value 		= models.TextField(max_length=255,blank=True,null=True)
# 	encrypted 	= models.BooleanField(default=False)
# 	exclude_from_report = models.BooleanField(default=False)
# 	source_system = models.TextField(max_length=255,blank=True,null=True)
# 	created_at 	= models.DateTimeField(auto_now_add=True)
# 	updated_at 	= models.DateTimeField(auto_now=True)

# 	def __str__(self):
# 		return self.metadata.field + ' - ' + self.value + ' - ' + self.request.email