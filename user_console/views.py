import csv
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import View,TemplateView,ListView,DetailView,FormView,UpdateView,CreateView
from django.http import HttpResponse, HttpResponseRedirect
from request_form_app.models import Company,Request,Consumer,Contact
from user_console.forms import RequestForm,CompanyForm
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_list_or_404,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from request_form_app.admin import RequestResource
from tablib import Dataset



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


# REQUEST VIEWS

class RequestListView(LoginRequiredMixin,TemplateView):

	model = Request

	context_object_name = 'request_list'
	template_name = 'user_console/request_list.html'

	login_url = '/console/login/'

	def get_context_data(self,**kwargs):
		context = super(RequestListView,self).get_context_data(**kwargs)
		context['todays_list'] = Request.objects.all()
		context['data_ready_to_send_list'] = Request.objects.filter(data_ready_to_send__iexact='yes')
		context['green_status_list'] = Request.objects.filter(status__iexact='green')
		context['yellow_status_list'] = Request.objects.filter(status__iexact='yellow')
		# context['orange_status_list'] = Request.objects.filter(status__iexact='orange')
		context['red_status_list'] = Request.objects.filter(status__iexact='red')
		return context

class RequestDetailView(LoginRequiredMixin,DetailView):

	model = Request

	# context_object_name = 'request_detail'

	template_name = 'user_console/request_detail.html'

	login_url = '/console/login/'

	# def get_context_data(self,**kwargs):
	# 	context = super(RequestListView,self).get_context_data(**kwargs)
	# 	context


class RequestUpdate(LoginRequiredMixin,UpdateView):
	
	model = Request
	template_name='user_console/request_update.html'
	form_class=RequestForm

	login_url = '/console/login/'

	# success_url = reverse_lazy('user_console:request_detail')

	def form_valid(self,form):
		pk = self.kwargs.get('pk')
		obj = get_object_or_404(Request, pk=pk)
		return super().form_valid(form)

		# return HttpResponseRedirect(reverse_lazy('user_console:request_detail',kwargs={'pk':self.pk}))

class RequestCreateView(LoginRequiredMixin,CreateView):
	model = Request
	form_class = RequestForm
	template_name = 'user_console/request_form.html'


	login_url = '/console/login/'

	def form_valid(self,form):
		# request = form.save()

		# send_mail('Hello from Braveheart Data!',
		# 	'This is the automated message. <b r> This is a test message',
		# 	'support@braveheartdata.com',
		# 	[case.email],
		# 	fail_silently=False)

		return super().form_valid(form)

		return HttpResponseRedirect(reverse('request_form_app:request_detail',kwargs={'pk':self.pk}))

# def RequestExportRedirect(request):
# 	retrun HttpResponseRedirect('requests/export-all')


# class ExportCompanyRequestsView(LoginRequiredMixin,View):




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
			

# class RequestExport(LoginRequiredMixin,View):

# 	template_name = 'export_requests.html'

	
# 	def form_valid(self,request):

# 		request_resource = RequestResource()
# 		dataset = request_resource.export()
# 		response = HttpResponse(dataset.csv,content_type='text/csv')
# 		response['Content-Disposition'] = 'attachment;filename="request.csv'
# 		return response