from django.db import models
from django.urls import reverse
from localflavor.us.models import USStateField, USSocialSecurityNumberField, USZipCodeField

from datetime import datetime,date
from datetime import timedelta

# Create your models here.

class Consumer(models.Model):

	ready_for_send_choices=(
		('yes','Yes'),
		('no','No')
		)

	first_name = models.CharField(max_length=256,blank=True)
	last_name = models.CharField(max_length=256,blank=False)
	email = models.EmailField(max_length=256,blank=True,unique=True)
	alternative_email = models.EmailField(max_length=256,blank=True)
	primary_address = models.CharField(max_length=256,blank=True)
	primary_address_line_two = models.CharField(max_length=256,blank=True)
	primary_city = models.CharField(max_length=256,blank=True)
	primary_state = USStateField(null=True,blank=True)
	primary_zip = USZipCodeField(null=True,blank=True)
	primary_country = models.CharField(max_length=256,blank=True)
	alternative_address = models.CharField(max_length=256,blank=True)
	alternative_address_line_two = models.CharField(max_length=256,blank=True)
	alternative_city = models.CharField(max_length=256,blank=True)
	alternative_state = models.CharField(max_length=256,blank=True)
	alternative_zip = USZipCodeField(null=True,blank=True)
	alternative_country = models.CharField(max_length=256,blank=True)
	# ssn = models.CharField(max_length=9,blank=True)
	ssn = USSocialSecurityNumberField(null=True,blank=True)
	driver_license_number = models.CharField(max_length=10,blank=True)
	driver_license_state = models.CharField(max_length=2,blank=True)
	date_of_birth = models.DateField(null=True,blank=True)
	terms_of_service_signed = models.BooleanField(default=False)
	identity_verified = models.BooleanField(default=False,null=True)
	# last_signed_terms_of_service_date = models.DateField(null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	phone = models.CharField(max_length=13,blank=True)
	alternative_phone = models.CharField(max_length=13,blank=True)


	def __str__(self):
		return self.first_name + " " + self.last_name

	def get_absolute_url(self):
		return reverse('user_console:consumer_detail',kwargs={'pk':self.pk})


class Company(models.Model):

	company_name = models.CharField(max_length=256,blank=False)
	legal_name = models.CharField(max_length=256,blank=True)
	website = models.URLField(max_length=200)
	primary_contact = models.ForeignKey('Contact',on_delete=models.CASCADE,null=True,blank=True)
	address 	= models.TextField(max_length=255,blank=True,null=True)
	address_line_two = models.TextField(max_length=255,blank=True,null=True)
	city 		= models.TextField(max_length=255,blank=True,null=True)
	state 		= USStateField(null=True,blank=True)
	zip_code 	= USZipCodeField(null=True,blank=True)
	country 	= models.CharField(max_length=256,blank=True)
	logo 		= models.ImageField(upload_to='request_form_app/company_logo',height_field='logo_height',width_field='logo_width',null=True,blank=True)
	logo_height = models.IntegerField(blank=True,null=True)
	logo_width  = models.IntegerField(blank=True,null=True)
	company_code = models.TextField(max_length=6,blank=True,null=True)


	def __str__(self):
		return self.company_name

	def get_absolute_url(self):
		return reverse('user_console:company_detail',kwargs={'pk':self.pk})

class Contact(models.Model):

	first_name = models.CharField(max_length=256,blank=False)
	last_name = models.CharField(max_length=256,blank=False)
	works_for = models.ForeignKey(Company,on_delete=models.CASCADE)
	phone = models.CharField(max_length=13,blank=True)
	alternative_phone = models.CharField(max_length=13,blank=True)

	def __str__(self):
		return self.first_name + " " + self.last_name

class Request(models.Model):

	request_source_choices = (
		('none','None'),
		('email','Email'),
		('phone','Phone'),
		('web','Web')
		)
	priority_choices = (
		('low','Low'),
		('medium','Medium'),
		('high','High')
		)
	stage_choices = (
		('new','New'),
		('in progress','In Progress'),
		('ready to review','Ready for Review'),
		('ready for consumer','Ready for Consumer'),
		('completed', 'Completed'),
		('past due', 'Past Due')
		)

	request_choices = (
		('yes','Yes please'),
		('no', 'Not right now')
		)

	data_ready_to_send_choices = (
		('yes','Yes'),
		('no','No')
		)

	status_choices = (
		('green','Green'),
		('yellow','Yellow'),
		('orange','Orange'),
		('red','Red'),
		)

	consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE,null=True,blank=True)
	company_requested = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
	request_source = models.CharField(max_length=20,choices=request_source_choices,default='none',blank=True)
	website_source = models.URLField(max_length=200,blank=True)
	delete_request = models.CharField(max_length=5,choices=request_choices,default='no',blank=True)
	what_request = models.CharField(max_length=5,choices=request_choices,default='no',blank=True)
	who_request = models.CharField(max_length=5,choices=request_choices,default='no',blank=True)
	opt_out_request = models.CharField(max_length=5,choices=request_choices,default='no',blank=True)
	priority = models.CharField(max_length=10,choices=priority_choices,default='low')
	escalated = models.BooleanField(null=True)
	stage = models.CharField(max_length=20,choices=stage_choices,default='new',blank=True)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	first_name = models.CharField(max_length=256,blank=False)
	last_name = models.CharField(max_length=256,blank=False)
	email = models.EmailField(max_length=256,blank=False)
	alternative_email = models.EmailField(max_length=256,blank=True)
	phone = models.CharField(max_length=13,blank=True)
	alternative_phone = models.CharField(max_length=13,blank=True)
	primary_address = models.CharField(max_length=256,blank=True)
	primary_address_line_two = models.CharField(max_length=256,blank=True)
	primary_city = models.CharField(max_length=256,blank=True)
	primary_state = USStateField(null=True,blank=True)
	primary_zip = USZipCodeField(null=True,blank=True)
	primary_country = models.CharField(max_length=256,blank=True)
	alternative_address = models.CharField(max_length=256,blank=True)
	alternative_address_line_two = models.CharField(max_length=256,blank=True)
	alternative_city = models.CharField(max_length=256,blank=True)
	alternative_state = models.CharField(max_length=256,blank=True)
	alternative_zip = models.CharField(max_length=256,blank=True)
	alternative_country = models.CharField(max_length=256,blank=True)
	ssn = USSocialSecurityNumberField(null=True,blank=True)
	driver_license_number = models.CharField(max_length=10,blank=True)
	driver_license_state = models.CharField(max_length=2,blank=True)
	date_of_birth = models.DateField(null=True,blank=True)
	terms_of_service_signed = models.BooleanField(default=False)
	data_ready_to_send = models.CharField(max_length=5,choices=data_ready_to_send_choices,default='no',blank=True)
	status = models.CharField(max_length=10,choices=status_choices,default='green',blank=True)
	days_open = models.IntegerField(default='1',blank=True,null=True)
	# date = models.DateField(default=date.today())

	def __str__(self):
		return self.first_name + self.last_name + " (" + self.email + ")"

	def get_absolute_url(self):
		return reverse("user_console:request_detail",kwargs={'pk':self.pk})

	def save(self,*args,**kwargs):

		if Consumer.objects.filter(email__iexact=self.email).exists():
			self.consumer = Consumer.objects.get(email__iexact=self.email)
						
		else:
			consumer = Consumer(first_name=self.first_name,last_name=self.last_name,email=self.email)
			consumer.save()
			
		return super().save(*args,**kwargs)








