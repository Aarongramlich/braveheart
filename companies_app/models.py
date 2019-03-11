from django.db import models
from localflavor.us.models import USStateField, USSocialSecurityNumberField, USPostalCodeField

class Company(models.Model):

	payment_terms_choices = (
		('7 days','7 Days'),
		('14 days', '14 Days'),
		('30 days','30 Days'),
		('60 days','60 Days')
		)

	payment_type_choices = (
		('credit card','Credit Card'),
		('bank transfer','Bank Transfer'),
		('direct deposit','Direct Deposit'),
		('check','Check'),
		)

	industry_choices = (
		('not sure','Not Sure'),
		('aerospace','Aerospace'),
		('advertising','Advertising'),
		('agriculture','Agriculture'),
		('apparel','Apparel'),
		('banking','Banking'),
		('business services','Business Services'),
		('biotechnology','Biotechnology'),
		('chemicals','Chemicals'),
		('communications','Communications'),
		('consulting','Consulting'),
		('education','Education'),
		('electronics','Electronics'),
		('energy','Energy'),
		('engineering','Engineering'),
		('entertainment','Entertainment'),
		('environmental','Environmental'),
		('finance','Finance'),
		('food and beverage','Food & Beverage'),
		('government','Government'),
		('healthcare','Healthcare'),
		('hospitality','Hospitality'),
		('insurance','Insurance'),
		('machinary','Machinary'),
		('manufacturing','Manufacturing'),
		('media','Media'),
		('not for profit','Not For Profit'),
		('other','Other'),
		('recreation','Recreation'),
		('retail','Retail'),
		('shipping','Shipping'),
		('technology','Technology'),
		('telecommunications','Telecommunications'),
		('transportation','Transportation'),
		('utilities','Utilities'),
		)

	company_name = models.CharField(max_length=256)
	website = models.URLField(max_length=256,blank=True)
	primary_address = models.CharField(max_length=256,blank=True)
	primary_address_line_two = models.CharField(max_length=256,blank=True)
	primary_city = models.CharField(max_length=256,blank=True)
	primary_state = models.CharField(max_length=256,blank=True)
	primary_zip = models.CharField(max_length=256,blank=True)
	primary_country = models.CharField(max_length=256,blank=True)
	billing_address = models.CharField(max_length=256,blank=True)
	billing_address_line_two = models.CharField(max_length=256,blank=True)
	billing_city = models.CharField(max_length=256,blank=True)
	billing_state = models.CharField(max_length=256,blank=True)
	billing_zip = models.CharField(max_length=256,blank=True)
	billing_country = models.CharField(max_length=256,blank=True)
	payment_terms = models.CharField(max_length=10,choices=payment_terms_choices,default='30 days')
	payment_type = models.CharField(max_length=20,choices=payment_type_choices,default='credit card')
	# primary_phone = models.CharField()
	primary_phone_ext = models.CharField(max_length=6,blank=True)
	active = models.BooleanField()
	notes = models.TextField(max_length=5000,blank=True)
	employees = models.CharField(max_length=6,blank=True)
	industry = models.CharField(max_length=50,choices=industry_choices,default='not sure')




	arr = models.DecimalField(max_digits=7,decimal_places=2)




# class Contact(models.Model):
