import csv,io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import View,TemplateView,ListView,DetailView,FormView,UpdateView,CreateView
from django.contrib.auth.decorators import permission_required 

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RequestResponse
from django.http import HttpResponse

from .utils import render_to_pdf

from request_form_app.models import Request,Company


# Create your views here.

@permission_required('admin.admin')
def request_response_upload(request):   #https://www.youtube.com/watch?v=BppyfPye8eo
	template = "request_response_upload.html"

	prompt = {
		'order': 'Order of the CSV should be first_name,last_name,email'
	}


# def generate_pdf(self, request,*args,**kwargs):
# 	template='request_response/response.html'
# 	context = {
# 		"request_id": self.request.id,
# 		"company_name": self.request.compandy_requested
# 	}

# 	pdf = render_to_pdf(template,context)

# 	if pdf:
# 			response = HttpResponse(pdf,content_type='application/pdf')
# 			filename = "PrivacyRequest_%s.pdf" %("1234")
# 			content = "inline; filename='%s'" %(filename)
# 			response['Content-Disposition'] = content
# 			return response 
# 	return HttpResponse("Not Found")

class GeneratePdf(DetailView):

	model = Request
	template_name='request_response/response.html'

	def get(self, request, *args, **kwargs):
		
		# context = super(GeneratePdf,self).get(request,*args,**kwargs)
		# return context

		context = {
			'first_name': 'Dave',
			'last_name': 'Lee',
			'email': 'david.lee@gmail1.com',
			'email_2': 'davel87@gmail1.com',
			'address': '201 Warner Ave',
			'address_2': 'Apt A201',
			'city': 'Los Angeles',
			'state': 'CA',
			'zip': '92716',
			'country': 'US',
			'annual_income': '$100,000-$150,000',
			'household_income': '$300,000-$500,000',
			'marketing_score': '87.6',
			'marketing_grade': 'B+',
			'last_activity': '09/28/18',
			'ip_address': '172.16.52.63',
			'customer_id': '1291840',
			'net_revenue': '$1,248.50',
			'interests': 'Golf, Cars',
			'relationship_status': 'Married',
			 }
		pdf = render_to_pdf('request_response/response.html',context)
        
		if pdf:
			response = HttpResponse(pdf,content_type='application/pdf')
			filename = "PrivacyRequest_%s.pdf" %("1234")
			content = "inline; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		# return HttpResponse("Not Found")

	# def get_context_data(self,request,*args,**kwargs):
	# 	context = super(GeneratePDF,self).get_context_data(*args,**kwargs)
	# 	context['response_object'] = Request.objects.filter(pk=self.object.pk)
	# 	return context



# class GeneratePdf(View):

# 	model = Request
	


	# def get(self, request, *args, **kwargs):


	# 	request_object = Request.objects.filter(id=self.object.id)
		
	# 	context = {
	# 		'request_name': request_object.first_name,
	# 		'today': "Today", 
	# 		'amount': 39.99,
	# 		'customer_name': 'Cooper Mann',
	# 		'order_id': 1233434,
	# 		 }
	# 	pdf = render_to_pdf('request_response/response.html', context)
        
	# 	if pdf:
	# 		response = HttpResponse(pdf,content_type='application/pdf')
	# 		filename = "PrivacyRequest_%s.pdf" %("1234")
	# 		content = "inline; filename='%s'" %(filename)
	# 		response['Content-Disposition'] = content
	# 		return response
	# 	return HttpResponse("Not Found")

		# https://www.youtube.com/watch?v=B7EIK9yVtGY