from django.db import models
from localflavor.us.models import USStateField, USSocialSecurityNumberField, USPostalCodeField

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
	email = models.EmailField(max_length=256,blank=False)
	alternative_email = models.EmailField(max_length=256,blank=True)
	# phone = models.PhoneField FIGURE OUT BEST WAY TO STORE PHONE
	# alternative_phone = models.PhoneField FIGURE OUT BEST WAY TO STORE PHONE
	primary_address = models.CharField(max_length=256,blank=True)
	primary_address_line_two = models.CharField(max_length=256,blank=True)
	primary_city = models.CharField(max_length=256,blank=True)
	primary_state = models.CharField(max_length=256,blank=True)
	primary_zip = models.CharField(max_length=256,blank=True)
	primary_country = models.CharField(max_length=256,blank=True)
	alternative_address = models.CharField(max_length=256,blank=True)
	alternative_address_line_two = models.CharField(max_length=256,blank=True)
	alternative_city = models.CharField(max_length=256,blank=True)
	alternative_state = models.CharField(max_length=256,blank=True)
	alternative_country = models.CharField(max_length=256,blank=True)
	ssn = models.CharField(max_length=9,blank=True)
	driver_license_number = models.CharField(max_length=10,blank=True)
	driver_license_state = models.CharField(max_length=2,blank=True)
	date_of_birth = models.DateField(blank=True)

	def __str__(self):
		return self.first_name + self.last_name

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

	consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
	request_source = models.CharField(max_length=20,choices=request_source_choices,default='none')
	delete_request = models.BooleanField(null=True)
	what_request = models.BooleanField(null=True)
	who_request = models.BooleanField(null=True)
	opt_out_request = models.BooleanField(null=True)	
	priority = models.CharField(max_length=10,choices=priority_choices,default='low')
	escalated = models.BooleanField(null=True)
	status = models.CharField(max_length=20,choices=status_choices,default='new')
	created_date_time = models.DateField(auto_now_add=True)
	# days_open = models.CharField()

