from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from request_form_app.models import Consumer,Case
from request_form_app.forms import CaseForm,ConsumerForm
from django.views.generic import (View, TemplateView, ListView, DetailView, 
									CreateView,DeleteView,UpdateView,FormView)
from django.urls import reverse, reverse_lazy

# Create your views here.

class CaseCreateView(CreateView):

	model = Case
	form_class = CaseForm

class CaseDetailView(DetailView):
	model = Case
	template_name = 'request_form_app/case_detail.html'	

	def consumer_dupe_check(request,email,pk):
		pass
