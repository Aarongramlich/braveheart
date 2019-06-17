import csv,io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import View,TemplateView,ListView,DetailView,FormView,UpdateView,CreateView
from django.contrib.auth.decorators import permission_required,login_required 
from .forms import RequestResponseForm,ResponseDataForm

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RequestResponse,ResponseData,ResponseCategory
from django.http import HttpResponse

from .utils import render_to_pdf
from easy_pdf.views import PDFTemplateView

from request_form_app.models import Request,Company


# Create your views here.

@login_required()
def request_response_upload(request):   #https://www.youtube.com/watch?v=BppyfPye8eo
	template = "request_response_upload.html"

	prompt = {
		'order': 'Order of the CSV should be first_name,last_name,email'
	}

# def RequestResponseCreateView(request):
# 	if request.method == 'POST':
# 		form = RequestResponseForm(request.POST,request.FILES)
# 		if form.is_valid():
# 			form.save()
# 		else:
# 			form = RequestResponseForm()
# 		return render(request,'request_response/request_response_form.html',{'form',form})

class RequestResponseCreateView(LoginRequiredMixin,CreateView):


	model=RequestResponse



	form_class = RequestResponseForm
	template_name = 'request_response/request_response_form.html'

	success_url = '/console/requests/'

	# def form_valid(self,form):
	# 	if request.method == 'POST':
	# 		form = RequestResponseForm(request.POST,request.FILES)
	# 		if form.is_valid():
	# 			Response = form.save(commit=False)
	# 			Response.request = self.pk
	# 			Response.company = self.pk.company__id
	# 			Response.save()
	# 	else:
	# 		form = RequestResponseForm()
	# 	return render(request,template_name,{'form',form})

	# 	Response = form.save(commit=False)
	# 	Response.request = self.pk
	# 	Response.company = self.pk.company__id
	# 	Response.save()


	

	# initial = {
	# 	'request': get_context_data('pk').default_request,
	# 	'company': initial_values('company__id').default_company,
	# 	}	



	login_url='/console/login'


class RequestResponseDetailView(LoginRequiredMixin,DetailView):
	model = RequestResponse
	

	login_url='/console/login'



class ResponseDataCreateView(LoginRequiredMixin,CreateView):

	model = ResponseData

	form_class = ResponseDataForm
	template_name = 'request_response/response_data_form.html'

	success_url = '/console/requests/'


class ResponseDataDetailView(LoginRequiredMixin,DetailView):
	model = ResponseData
	template = "response_data_detail.html"

	login_url='/console/login'


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


class TestPdf(PDFTemplateView):
	template_name='request_response/response_pdf.html'


	def get_context_data(self,**kwargs):

		context = super(TestPdf,self).get_context_data(**kwargs)
		
		pk = self.kwargs.get('pk')
		

		
		
		self.company = self.kwargs.get('company')

		context['response_data'] = ResponseData.objects.filter(request_response__id=pk)
		context['personal_response_data'] = ResponseData.objects.filter(request_response__id=pk,metadata__data_category__iexact='personal')
		context['employment_response_data'] = ResponseData.objects.filter(request_response__id=pk,metadata__data_category__iexact='employment')
		context['geolocation_response_data'] = ResponseData.objects.filter(request_response__id=pk,metadata__data_category__iexact='geolocation')
		context['inferred_response_data'] = ResponseData.objects.filter(request_response__id=pk,metadata__data_category__iexact='inferred')
		context['commercial_response_data'] = ResponseData.objects.filter(request_response__id=pk,metadata__data_category__iexact='commercial')
		context['biometric_response_data'] = ResponseData.objects.filter(request_response__id=pk,metadata__data_category__iexact='biometric')
		context['internet_response_data'] = ResponseData.objects.filter(request_response__id=pk,metadata__data_category__iexact='internet')
		context['psychometric_response_data'] = ResponseData.objects.filter(request_response__id=pk,metadata__data_category__iexact='psychometric')
		context['sensory_response_data'] = ResponseData.objects.filter(request_response__id=pk,metadata__data_category__iexact='sensory')
		context['data_source_category_list'] = ResponseCategory.objects.filter(request_response__id=pk,data_category__category_type__iexact='source')
		context['vendor_category_list'] = ResponseCategory.objects.filter(request_response__id=pk,data_category__category_type__iexact='vendor')
		context['data_category_list'] = ResponseCategory.objects.filter(request_response__id=pk,data_category__category_type__iexact='data')

		context['response_company'] = Company.objects.filter() ##THIS WON'T WORK -- FIX 
		return context


class GeneratePdf(DetailView):

	model = RequestResponse
	template_name='request_response/response.html'



	def get_context_data(self,**kwargs):

		context = super(GeneratePdf,self).get_context_data(**kwargs)
		
		pk = self.kwargs.get('pk')

		context['response_data'] = ResponseData.objects.filter(request_response__id=pk)
		return context
		return render_to_pdf('request_response/response.html',(response_data))


		# if pdf:
		# 	response = HttpResponse(pdf,content_type='application/pdf')
		# 	filename = "PrivacyRequest_%s.pdf" %(self.kwargs.get('pk'))
		# 	content = "inline; filename='%s'" %(filename)
		# 	response['Content-Disposition'] = content
		# 	return response
		# else:
		# 	print('No PDF found.')
		# return context 




	# def get(self, request, *args, **kwargs):
		
	# 	context = super(GeneratePdf,self).get(request,*args,**kwargs)
		# pk = self.kwargs.get('pk')
		
		# return context
 
		# context['request_object'] = Request.objects.filter(pk=pk)

		# context = {
		# 	'first_name': context.get('first_name'),
		# 	'last_name': 'Lee',
		# 	'email': 'david.lee@gmail1.com',
		# 	'email_2': 'davel87@gmail1.com',
		# 	'address': '201 Warner Ave',
		# 	'address_2': 'Apt A201',
		# 	'city': 'Los Angeles',
		# 	'state': 'CA',
		# 	'zip': '92716',
		# 	'country': 'US',
		# 	'annual_income': '$100,000-$150,000',
		# 	'household_income': '$300,000-$500,000',
		# 	'marketing_score': '87.6',
		# 	'marketing_grade': 'B+',
		# 	'last_activity': '09/28/18',
		# 	'ip_address': '172.16.52.63',
		# 	'customer_id': '1291840',
		# 	'net_revenue': '$1,248.50',
		# 	'interests': 'Golf, Cars',
		# 	'relationship_status': 'Married',
		# 	 }
		# pdf = render_to_pdf('request_response/response.html',(context))
        
		# if pdf:
		# 	response = HttpResponse(pdf,content_type='application/pdf')
		# 	filename = "PrivacyRequest_%s.pdf" %("1234")
		# 	content = "inline; filename='%s'" %(filename)
		# 	response['Content-Disposition'] = content
		# 	return response
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


def ResponseDataExport(request):
	response_resource = ResponseDataResource()
	dataset = request_resource.export()
	response = HttpResponse(dataset.csv,content_type='text/csv')
	response['Content-Disposition'] = 'attachment;filename=response_data.csv'
	return response

def ResponseDataImport(request):
	if request.method == 'POST':
		response_resource = ResponseDataResource()
		dataset = Dataset()
		new_responses = request.FILES['response_data_file']

		imported_data = dataset.load(new_responses.read())
		result = response_resource.import_data(dataset,dry_run=True)

		if not result.has_errors():
			response_resource.import_data(datase,dry_run=True)

	return render(request,'request_response/import_response_data.html')


