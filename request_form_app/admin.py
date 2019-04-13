from django.contrib import admin
from .models import Consumer,Case,Company,Contact

# Register your models here.

admin.site.register(Consumer)
admin.site.register(Case)
admin.site.register(Company)
admin.site.register(Contact)