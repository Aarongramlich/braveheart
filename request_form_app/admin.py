from django.contrib import admin
from .models import Consumer,Request,Company,Contact
from import_export import resources
from import_export.admin import ImportExportModelAdmin



# Register your models here.



class RequestResource(resources.ModelResource):

	class Meta:
		model = Request
		fields = ('id','company_requested','first_name','last_name','email','what_request','opt_out_request','who_request','delete_request','alternative_email',
					'phone','alternative_phone','primary_address','primary_city','primary_state',
					'primary_country','request_source','website_source')
		export_order = ('id','company_requested','first_name','last_name','email','what_request','opt_out_request','who_request','delete_request','alternative_email',
					'phone','alternative_phone','primary_address','primary_city','primary_state',
					'primary_country','request_source','website_source')


class RequestAdmin(ImportExportModelAdmin):
	resource_class = RequestResource

admin.site.register(Consumer)
admin.site.register(Request,RequestAdmin)
admin.site.register(Company)
admin.site.register(Contact)