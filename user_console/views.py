from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from request_form_app.models import Company,Request,Consumer,Contact

# Create your views here.

# class ProfileView(View):
# 	template_name='user_console/homepage.html'

class HomepageView(View):

	template_name = 'user_console/homepage.html'

	def get(self,request):

		return render(request,self.template_name)

class RequestListView(TemplateView):

	model = Request

	context_object_name = 'request_list'
	template_name = 'user_console/request_list.html'

	def get_context_data(self,**kwargs):
		context = super(RequestListView,self).get_context_data(**kwargs)
		context['todays_list'] = Request.objects.all()
		context['data_ready_to_send_list'] = Request.objects.filter(data_ready_to_send__iexact='yes')
		context['green_status_list'] = Request.objects.filter(status__iexact='green')
		context['yellow_status_list'] = Request.objects.filter(status__iexact='yellow')
		# context['orange_status_list'] = Request.objects.filter(status__iexact='orange')
		context['red_status_list'] = Request.objects.filter(status__iexact='red')
		return context

class ConsumerListView(ListView):

	model = Consumer

	context_object_name = 'consumer_list'
	template_name = 'user_console/consumer_list.html'

	
	# paginate_by = 15



	def get_context_data(self,**kwargs):
		context = super(ConsumerListView,self).get_context_data(**kwargs)
		context['everyone_list'] = Consumer.objects.all()
		return context


	# return render(request,'user_console/consumers_detail.html',)

class CompanyListView(TemplateView):
	context_object_name = 'company_list'
	template_name = 'user_console/companies_detail.html'

	model = Company
	paginate_by = 15

	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		return context