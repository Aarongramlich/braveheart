from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import View,TemplateView,ListView,DetailView,FormView,UpdateView
from django.http import HttpResponse
from request_form_app.models import Company,Request,Consumer,Contact
from user_console.forms import RequestForm
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_list_or_404,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

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

class CompanyListView(LoginRequiredMixin,TemplateView):
	context_object_name = 'company_list'
	template_name = 'user_console/companies_detail.html'

	model = Company
	paginate_by = 15

	login_url = '/console/login/'

	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		return context




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