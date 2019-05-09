from django.contrib import admin
from .models import Consumer,Request,Company,Contact

# Register your models here.

admin.site.register(Consumer)
admin.site.register(Request)
admin.site.register(Company)
admin.site.register(Contact)