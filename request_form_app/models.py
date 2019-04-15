from django.db import models
from django.urls import reverse
from localflavor.us.models import USStateField, USSocialSecurityNumberField, USZipCodeField

# Create your models here.

class Consumer(models.Model):

	# driver_license_state = (
	# 	('AL','AL'),
	# 	('AK','AK'),
	# 	('AR','AR'),
	# 	('CA','CA'),
	# 	('CO','CO'),
	# 	('CT','CT'),
	# 	('DE','DE'),
	# 	('FL','FL'),
	# 	('AL','AL'),
	# 	('AL','AL'),
	# 	('AL','AL'),
	# 	('AL','AL'),
	# 	('AL','AL'),
	# 	('AL','AL'),
	# 	('AL','AL'),
	# 	('AL','AL'),
	# 	('AL','AL'),
	# 	('AL','AL'),

	# 	)


	first_name = models.CharField(max_length=256,blank=True)
	last_name = models.CharField(max_length=256,blank=False)
	email = models.EmailField(max_length=256,blank=True)
	alternative_email = models.EmailField(max_length=256,blank=False)
	# phone = models.PhoneField FIGURE OUT BEST WAY TO STORE PHONE
	# alternative_phone = models.PhoneField FIGURE OUT BEST WAY TO STORE PHONE
	primary_address = models.CharField(max_length=256,blank=True)
	primary_address_line_two = models.CharField(max_length=256,blank=True)
	primary_city = models.CharField(max_length=256,blank=True)
	# primary_state = models.CharField(max_length=256,blank=True) REPLACED WITH LOCALFLAVOR FIELD
	primary_state = USStateField(blank=True)
	# primary_zip = models.CharField(max_length=256,blank=True) REPLACED WITH LOCALFLAVOR FIELD
	primary_zip = USZipCodeField(blank=True)
	primary_country = models.CharField(max_length=256,blank=True)
	alternative_address = models.CharField(max_length=256,blank=True)
	alternative_address_line_two = models.CharField(max_length=256,blank=True)
	alternative_city = models.CharField(max_length=256,blank=True)
	alternative_state = models.CharField(max_length=256,blank=True)
	alternative_country = models.CharField(max_length=256,blank=True)
	# ssn = models.CharField(max_length=9,blank=True)
	ssn = USSocialSecurityNumberField(null=True,blank=True)
	driver_license_number = models.CharField(max_length=10,blank=True)
	driver_license_state = models.CharField(max_length=2,blank=True)
	date_of_birth = models.DateField(null=True,blank=True)
	terms_of_service_signed = models.BooleanField(default=False)
	last_signed_terms_of_service_date = models.DateField(null=True,blank=True)

	def __str__(self):
		return self.first_name + " " + self.last_name

	def get_absolute_url(self):
		return reverse('request_form_app:case_detail',kwargs={'pk':self.pk})


class Company(models.Model):

	company_name = models.CharField(max_length=256,blank=False)
	website = models.URLField(max_length=200)
	primary_contact = models.ForeignKey('Contact',on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return self.company_name

class Contact(models.Model):

	first_name = models.CharField(max_length=256,blank=False)
	last_name = models.CharField(max_length=256,blank=False)
	works_for = models.ForeignKey(Company,on_delete=models.CASCADE)

	def __str__(self):
		return self.first_name + " " + self.last_name

class Case(models.Model):

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
	status_choices = (
		('new','New'),
		('in progress','In Progress'),
		('completed', 'Completed'),
		('past due', 'Past Due')
		)

	request_choices = (
		('yes','Yes please'),
		('no', 'Not right now')
		)

	consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE,null=True,blank=True)
	company_requested = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
	request_source = models.CharField(max_length=20,choices=request_source_choices,default='none')
	website_source = models.URLField(max_length=200,blank=True)
	delete_request = models.CharField(max_length=5,choices=request_choices,default='no')
	what_request = models.CharField(max_length=5,choices=request_choices,default='no')
	who_request = models.CharField(max_length=5,choices=request_choices,default='no')
	opt_out_request = models.CharField(max_length=5,choices=request_choices,default='no')
	priority = models.CharField(max_length=10,choices=priority_choices,default='low')
	escalated = models.BooleanField(null=True)
	status = models.CharField(max_length=20,choices=status_choices,default='new')
	created_date_time = models.DateField(auto_now_add=True)
	# days_open = models.CharField()
	# verified_request = models.BooleanField(null=True)

	first_name = models.CharField(max_length=256,blank=False)
	last_name = models.CharField(max_length=256,blank=False)
	email = models.EmailField(max_length=256,blank=False)
	alternative_email = models.EmailField(max_length=256,blank=True)
	# phone = models.PhoneField FIGURE OUT BEST WAY TO STORE PHONE
	# alternative_phone = models.PhoneField FIGURE OUT BEST WAY TO STORE PHONE
	primary_address = models.CharField(max_length=256,blank=True)
	primary_address_line_two = models.CharField(max_length=256,blank=True)
	primary_city = models.CharField(max_length=256,blank=True)
	# primary_state = models.CharField(max_length=256,blank=True) REPLACED WITH LOCALFLAVOR FIELD
	primary_state = USStateField(null=True,blank=True)
	# primary_zip = models.CharField(max_length=256,blank=True) REPLACED WITH LOCALFLAVOR FIELD
	primary_zip = USZipCodeField(null=True,blank=True)
	primary_country = models.CharField(max_length=256,blank=True)
	alternative_address = models.CharField(max_length=256,blank=True)
	alternative_address_line_two = models.CharField(max_length=256,blank=True)
	alternative_city = models.CharField(max_length=256,blank=True)
	alternative_state = models.CharField(max_length=256,blank=True)
	alternative_country = models.CharField(max_length=256,blank=True)
	# ssn = models.CharField(max_length=9,blank=True)
	ssn = USSocialSecurityNumberField(null=True,blank=True)
	driver_license_number = models.CharField(max_length=10,blank=True)
	driver_license_state = models.CharField(max_length=2,blank=True)
	date_of_birth = models.DateField(null=True,blank=True)
	terms_of_service_signed = models.BooleanField(default=False)
	# terms_of_service_signed_date = models.DateField(null=True,blank=True)

	def __str__(self):
		return self.first_name + self.last_name + " (" + self.email + ")"

	def get_absolute_url(self):
			return reverse('request_form_app:case_detail',kwargs={'pk':self.pk})
