import csv,io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import View,TemplateView,ListView,DetailView,FormView,UpdateView,CreateView
from django.contrib.auth.decorators import permission_required,login_required 
from .forms import RequestResponseForm,ResponseDataForm,ResponseCategoryForm

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RequestResponse,ResponseData,ResponseCategory
from response_metadata.models import Metadata
from django.http import HttpResponse

from .utils import render_to_pdf
from easy_pdf.views import PDFTemplateView
from tablib import Dataset

from request_form_app.models import Request,Company
from request_response.admin import ResponseDataResource


# Create your views here.

@login_required()
def request_response_upload(request):   #https://www.youtube.com/watch?v=BppyfPye8eo
	template = "request_response/request_response_upload.html"

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

	

	login_url='/console/login'

	def form_valid(self,form):
		
		return super().form_valid(form)

	def get_initial(self,**kwargs):
	    
	    

	    initial = super().get_initial(**kwargs)

	    pk = self.kwargs.get('pk')
	    request_record = Request.objects.get(pk=pk)

	    initial['request'] = pk
	    initial['company'] = request_record.company_requested
	    initial['email'] = request_record.email

	    return initial
	


class RequestResponseDetailView(LoginRequiredMixin,DetailView):
	model = RequestResponse
	
	template_name="request_response/request_response_detail.html"

	login_url='/console/login'





class ResponseDataCreateView(LoginRequiredMixin,CreateView):

	model = ResponseData

	form_class = ResponseDataForm
	template_name = 'request_response/response_data_form.html'

	success_url = '/console/requests/'

	def get_initial(self):
		initial = super().get_initial()

		pk = self.kwargs.get('pk')

		initial['request'] = pk
		return initial


	def form_valid(self,form):
		
		return super().form_valid(form)


class ResponseDataUpdateView(LoginRequiredMixin,UpdateView):
	model = ResponseData
	form_class = ResponseDataForm
	template_name = 'request_response/response_data_form.html'

	login_url = '/console/login/'



class RequestResponseUpdateView(LoginRequiredMixin,UpdateView):
	model = RequestResponse
	form_class = RequestResponseForm
	template_name = 'request_response/request_response_form.html'

	login_url = '/console/login/'



class ResponseDataDetailView(LoginRequiredMixin,DetailView):
	model = ResponseData
	template_name = "request_response/response_data_detail.html"

	login_url='/console/login'


class ResponseCategoryDetailView(LoginRequiredMixin,DetailView):
	model = ResponseCategory
	template_name = "request_response/response_category_detail.html"

	login_url='/console/login'

class ResponseCategoryCreateView(LoginRequiredMixin,CreateView):
	model = ResponseCategory
	form_class = ResponseCategoryForm
	template_name = 'request_response/response_category_form.html'

	success_url = '/console/requests/'

	def get_initial(self):
		initial = super().get_initial()

		pk = self.kwargs.get('pk')

		initial['request'] = pk
		return initial


	# def form_valid(self,form):
		
	# 	return super().form_valid(form)

class ResponseCategoryUpdateView(LoginRequiredMixin,UpdateView):
	model = ResponseCategory
	form_class = ResponseCategoryForm
	template_name = 'request_response/response_category_form.html'

	login_url = '/console/login/'


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



@permission_required('user.admin',login_url='/console/login/')
def ResponseDataExport(request):
	response_resource = ResponseDataResource()
	dataset = response_resource.export()
	response = HttpResponse(dataset.csv,content_type='text/csv')
	response['Content-Disposition'] = 'attachment;filename=response_data.csv'
	return response


# @permission_required('user.admin',login_url='/console/login/')
def ResponseDataImport(request):
	template='request_response/import_response_data.html'

	if request.method =='GET':
		return render(request,template)

	csv_file = request.FILES['responseFile']

	if not csv_file.name.endswith('.csv'):
		messages.error(request,'Please select a .csv file.')
	
	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string,delimiter=',',quotechar="|"):
		_, created = ResponseData.objects.update_or_create(
				id=column[0],
				metadata=Metadata.objects.get(metadata_key=column[1]),
				request=Request.objects.get(pk=column[2]),
				request_response=RequestResponse.objects.get(pk=column[3]),
				value=column[4],
				encrypted=column[5],
				exclude_from_report=column[6],
				source_system=column[7],

			)

	context = {}
	return render(request,template,context)





# def ResponseDataImport(request):
# 	if request.method == 'POST':
# 		response_resource = ResponseDataResource()
# 		dataset = Dataset()
# 		new_responses = request.FILES['response_data_file']

# 		imported_data = dataset.load(new_responses.read(),format='csv')
# 		result = response_resource.import_data(dataset,dry_run=True,)

# 		if not result.has_errors():
# 			response_resource.import_data(dataset,dry_run=True)

# 	return render(request,'request_response/import_response_data.html')


