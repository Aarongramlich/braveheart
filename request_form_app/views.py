from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from request_form_app.models import Consumer,Request
from request_form_app.forms import RequestForm,ConsumerForm
from django.views.generic import (View, TemplateView, ListView, DetailView, 
									CreateView,DeleteView,UpdateView,FormView)
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
# from request_form_app import urls

# Create your views here.

class RequestCreateView(CreateView):

	model = Request
	form_class = RequestForm
	def form_valid(self,form):
		
		return super().form_valid(form)

	def get_success_url(self):
		return reverse("request_form_app:request_detail",args=[self.object.pk])

	

		# return HttpResponseRedirect(reverse('request_form_app:request_detail',kwargs={'pk':self.pk}))
# SEE https://docs.djangoproject.com/en/2.2/topics/class-based-views/intro/ UNDERSTAND THIS

class RequestDetailView(DetailView):
	model = Request
	template_name = 'request_form_app/request_detail.html'
