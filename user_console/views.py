import csv
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import View,TemplateView,ListView,DetailView,FormView,UpdateView,CreateView
from django.http import HttpResponse, HttpResponseRedirect

from request_form_app.models import Company,Request,Consumer,Contact
from request_response.models import RequestResponse,ResponseData
from accounts.models import User

from request_response import urls

from user_console.forms import RequestForm,CompanyForm,ConsumerForm
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_list_or_404,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from request_form_app.admin import RequestResource
from tablib import Dataset
from datetime import date,timedelta,datetime,timezone





# Create your views here.

# class ProfileView(View):
# 	template_name='user_console/homepage.html'

class HomepageView(LoginRequiredMixin,View):

	template_name = 'user_console/homepage.html'

	login_url = '/console/login/'

	def get(self,request):

		return render(request,self.template_name)


# CONSUMER VIEWS

class ConsumerListView(LoginRequiredMixin,ListView):

	model = Consumer

	context_object_name = 'consumer_list'
	template_name = 'user_console/consumer_list.html'

	login_url = '/console/login/'

	
	# paginate_by = 15



	def get_context_data(self,**kwargs):
		context = super(ConsumerListView,self).get_context_data(**kwargs)
		context['everyone_list'] = Consumer.objects.all()
		return context


	# return render(request,'user_console/consumers_detail.html',)


class ConsumerCreateView(LoginRequiredMixin,CreateView):

	model = Consumer
	form_class= ConsumerForm
	template_name = 'user_console/consumer_form.html'

	login_url = '/console/login/'

	# def form_valid(form,self):
	# 	return super().form_valid(form)
	# 	form.save()

	def get_success_url(self):
		return reverse("user_console:consumer_detail",args=[self.object.pk])


# COMPANY VIEWS

class CompanyCreateView(LoginRequiredMixin,CreateView):
	model = Company
	form_class = CompanyForm
	template_name = 'user_console/company_form.html'

	def form_valid(self,form):
		# request = form.save()

		# send_mail('Hello from Braveheart Data!',
		# 	'This is the automated message. <b r> This is a test message',
		# 	'support@braveheartdata.com',
		# 	[case.email],
		# 	fail_silently=False)

		return super().form_valid(form)

		return HttpResponseRedirect(reverse('user_console:company_detail',kwargs={'pk':self.pk}))

class ConsumerDetailView(LoginRequiredMixin,DetailView):
	model = Consumer
	template_name = 'user_console/consumer_detail.html'

	login_url = '/console/login/'

class CompanyListView(LoginRequiredMixin,TemplateView):
	context_object_name = 'company_list'
	template_name = 'user_console/company_list.html'

	model = Company
	

	login_url = '/console/login/'

	def get_context_data(self,**kwargs):
		context=super(CompanyListView,self).get_context_data(**kwargs)

		context['all_companies_list'] = Company.objects.all()

		return context

class CompanyDetailView(LoginRequiredMixin,DetailView):
	model = Company
	template_name = 'user_console/company_detail.html'

	login_url = '/console/login/'

	def get_context_data(self, **kwargs):
		context = super(CompanyDetailView,self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk')
		context['related_requests_list'] = Request.objects.filter(company_requested_id=pk)
		return context




# REQUEST VIEWS

class RequestListView(LoginRequiredMixin,TemplateView):

	model = Request

	context_object_name = 'request_list'
	template_name = 'user_console/request_list.html'

	login_url = '/console/login/'

	

	def get_context_data(self,**kwargs):

		today = date.today()
		last_week = date.today() + timedelta(days=-7)

		context = super(RequestListView,self).get_context_data(**kwargs)
		context['all_requests_list'] = Request.objects.filter(company_requested__in = self.request.user.company.all()).order_by('-created_at')
		context['todays_list'] = Request.objects.filter(created_at__year=today.year,created_at__month=today.month,created_at__day=today.day,company_requested__in = self.request.user.company.all())
		context['not_started_list'] = Request.objects.filter(stage__iexact='new',company_requested__in = self.request.user.company.all())
		context['last_week_list'] = Request.objects.filter(created_at__gte=date.today()+timedelta(days=-7),company_requested__in = self.request.user.company.all())
		context['ready_for_review_list'] = Request.objects.filter(stage__iexact='ready to review',company_requested__in = self.request.user.company.all())
		context['data_ready_to_send_list'] = Request.objects.filter(stage__iexact='ready for consumer',company_requested__in = self.request.user.company.all())
		context['green_status_list'] = Request.objects.filter(status__iexact='green',company_requested__in = self.request.user.company.all())
		context['yellow_status_list'] = Request.objects.filter(status__iexact='yellow',company_requested__in = self.request.user.company.all())
		# context['orange_status_list'] = Request.objects.filter(status__iexact='orange')
		context['red_status_list'] = Request.objects.filter(status__iexact='red',company_requested__in = self.request.user.company.all())
		return context

class RequestDetailView(LoginRequiredMixin,DetailView):

	model = Request

	# context_object_name = 'request_detail'

	template_name = 'user_console/request_detail.html'

	login_url = '/console/login/'

	def get_context_data(self,**kwargs):
		context = super(RequestDetailView,self).get_context_data(**kwargs)
		pk=self.kwargs.get('pk')
		context['request_response_list']=RequestResponse.objects.filter(request__id=pk)
		context['response_data_list']=ResponseData.objects.filter(request__id=pk)
		return context

	




class RequestUpdate(LoginRequiredMixin,UpdateView):
	
	model = Request
	fields = ['consumer',
		'company_requested',
		'request_source',
		'website_source',
		'what_request',
		'who_request',
		'opt_out_request',
		'delete_request',
		'priority',
		'escalated',
		'stage',
		'first_name',
		'last_name',
		'email',
		'alternative_email',
		'phone',
		'alternative_phone',
		'primary_address',
		'primary_address_line_two',
		'primary_city',
		'primary_state',
		'primary_zip',
		'primary_country',
		'alternative_address',
		'alternative_address_line_two',
		'alternative_city',
		'alternative_state',
		'alternative_country',
		'ssn',
		'driver_license_number',
		'driver_license_state',
		'date_of_birth',
		'terms_of_service_signed',
		'data_ready_to_send',
		'status',
		'days_open',]
	template_name_suffix='_update_form'


	login_url = '/console/login/'

	
	
	# def form_valid(self,form):
	# 	return super(RequestUpdate,self.object).form_valid(form)
	# 	self.object.form.save()

	# 	# self.object = form.save()
	# 	return HttpResponseRedirect(self.object.get_success_url())

	# def get_success_url(self):
	# 	return reverse("user_console:request_detail",args=[self.object.pk])

		# return HttpResponseRedirect(reverse_lazy('user_console:request_detail',kwargs={'pk':self.pk}))

	# success_url = reverse_lazy('user_console:request_detail')

	# def form_valid(self,form):
	# 	pk = self.kwargs.get('pk')
	# 	obj = get_object_or_404(Request, pk=pk)
	# 	return super().form_valid(form)



		# pk.save()

	

class RequestCreateView(LoginRequiredMixin,CreateView):
	model = Request
	form_class = RequestForm
	template_name = 'user_console/request_form.html'

	login_url = '/console/login/'

	
	
		
	def get_success_url(self):
		return reverse("user_console:request_detail",args=[self.object.pk])



def RequestExport(request):

		request_resource = RequestResource()
		dataset = request_resource.export()
		response = HttpResponse(dataset.csv,content_type='text/csv')
		response['Content-Disposition'] = 'attachment;filename="request.csv'
		return response

def RequestImport(request):
	if request.method == 'POST':
		request_resource = RequestResource()
		dataset = Dataset()
		new_requests = request.FILES['request_file']

		imported_data = dataset.load(new_requests.read())
		result = request_resource.import_data(dataset,dry_run=True)

		if not result.has_errors():
			request_resource.import_data(dataset,dry_run=True)

	return render(request,'user_console/import_requests.html')
			


