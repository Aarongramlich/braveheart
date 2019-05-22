from django.db import models
from request_form_app.models import Company
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)


# Create your models here.

class UserManager(BaseUserManager):
	def create_user(self,email,last_name,password=None,is_active=True,is_staff=False,is_admin=False):
		if not email:
			raise ValueError("Users must enter an email address")

		if not last_name:
			raise ValueError("Users must enter a last name")

		if not password:
			raise ValueError("Users must have a password")

		user = self.model(
			email = self.normalize_email(email),
			last_name = last_name,
			)

		user.set_password(password)
		user.staff = is_staff
		user.active = is_active
		user.admin = is_admin

		user.save(using=self._db)
		return user

	def create_staffuser(self,email,last_name,password=None,is_active=True,is_staff=True,is_admin=False):
		if not email:
			raise ValueError("Users must enter an email address")

		if not last_name:
			raise ValueError("Users must enter a last name")

		if not password:
			raise ValueError("Users must have a password")

		user = self.model(
			email = self.normalize_email(email),
			last_name = last_name,
			)

		user.set_password(password)
		user.staff = is_staff
		user.active = is_active
		user.admin = is_admin

		user.save(using=self._db)
		return user


	def create_superuser(self,email,last_name,password=None,is_active=True,is_staff=True,is_admin=True):
		if not email:
			raise ValueError("Users must enter an email address")

		if not last_name:
			raise ValueError("Users must enter a last name")

		if not password:
			raise ValueError("Users must have a password")

		user = self.model(
			email = self.normalize_email(email),
			last_name = last_name,
			)

		user.set_password(password)
		user.staff = is_staff
		user.active = is_active
		user.admin = is_admin

		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	email		= models.EmailField(unique=True,max_length=255)
	first_name 	= models.CharField(max_length=255,blank=True,null=True)
	last_name	= models.CharField(max_length=255,blank=True,null=True)
	active		= models.BooleanField(default=True) #can login
	staff		= models.BooleanField(default=False)
	admin		= models.BooleanField(default=False) #superuser
	company		= models.ManyToManyField('request_form_app.Company',blank=True)
	confirmed_email = models.BooleanField(default=False) #set to true when email is confirmed by user
	notes		=	models.TextField(null=True,blank=True)

	phone = models.CharField(max_length=13,blank=True)

	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	USERNAME_FIELD = 'email' #username
	#username_field and password are required by default

	REQUIRED_FIELDS = ['last_name']

	objects = UserManager()

	def get_full_name(self):
		return '%s %s' % (self.first_name,self.last_name)

	def __str__(self):
		return self.email

	def has_perm(self,perm,object=None):
		return True

	def has_module_perms(self,app_label):
		return True

	@property
	def is_admin(self):
		return self.staff

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_active(self):
		return self.staff