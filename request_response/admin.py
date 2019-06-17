from django.contrib import admin
from .models import RequestResponse,ResponseData,ResponseCategory
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ResponseDataResource(resources.ModelResource):
	class Meta:
		model = ResponseData

		fields = ('id','metadata','request','request_response','value','encrypted','exclude_from_report','source_system')

		export_order = ('id','metadata','request','request_response','value','encrypted','exclude_from_report','source_system')

class ResponseDataAdmin(ImportExportModelAdmin):
	resource_class = ResponseDataResource

admin.site.register(RequestResponse)
admin.site.register(ResponseData,ResponseDataAdmin)
admin.site.register(ResponseCategory)