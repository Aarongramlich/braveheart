import csv
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import View,TemplateView,ListView,DetailView,FormView,UpdateView,CreateView
from django.http import HttpResponse, HttpResponseRedirect

from response_metadata.models import Metadata,MetadataCategory

from accounts.models import User

from request_response import urls

from response_metadata.forms import MetadataForm,MetadataCategoryForm
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_list_or_404,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from tablib import Dataset
from datetime import date,timedelta,datetime,timezone


# Create your views here.

class MetadataListView(LoginRequiredMixin,ListView):
	model = Metadata

	# context_object_name = 'metadata_list'
	template_name='response_metadata/metadata_list.html'

	login_url = '/console/login/'

	def get_context_data(self,**kwargs):

		context = super(MetadataListView,self).get_context_data(**kwargs)
		context['all_metadata_list'] = Metadata.objects.filter(company__in = self.request.user.company.all()).order_by('sequence')
		context['personal_meta_list']= Metadata.objects.filter(data_category__iexact='personal',company__in = self.request.user.company.all()).order_by('sequence')
		context['commercial_meta_list']= Metadata.objects.filter(data_category__iexact='commercial',company__in = self.request.user.company.all()).order_by('sequence')
		context['biometric_meta_list']= Metadata.objects.filter(data_category__iexact='biometric',company__in = self.request.user.company.all()).order_by('sequence')
		context['internet_meta_list']= Metadata.objects.filter(data_category__iexact='internet',company__in = self.request.user.company.all()).order_by('sequence')
		context['geolocation_meta_list']= Metadata.objects.filter(data_category__iexact='geolocation',company__in = self.request.user.company.all()).order_by('sequence')
		context['sensory_meta_list']= Metadata.objects.filter(data_category__iexact='sensory',company__in = self.request.user.company.all()).order_by('sequence')
		context['psychometric_meta_list']= Metadata.objects.filter(data_category__iexact='psychometric',company__in = self.request.user.company.all()).order_by('sequence')
		context['employment_meta_list']= Metadata.objects.filter(data_category__iexact='employment',company__in = self.request.user.company.all()).order_by('sequence')
		context['inferred_meta_list']= Metadata.objects.filter(data_category__iexact='inferred',company__in = self.request.user.company.all()).order_by('sequence')
		return context



class MetadataCreateView(LoginRequiredMixin,CreateView):
	model = Metadata
	form_class = MetadataForm
	template_name = 'response_metadata/metadata_form.html'

	login_url = '/console/login/'


class MetadataDetailView(LoginRequiredMixin,DetailView):
	model = Metadata
	template_name = 'response_metadata/metadata_detail.html'

	login_url = '/console/login/'




class MetadataUpdateView(LoginRequiredMixin,UpdateView):
	model = Metadata
	form_class = MetadataForm
	template_name = 'response_metadata/metadata_form.html'

	login_url = '/console/login/'

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)


class MetadataCategoryListView(LoginRequiredMixin,ListView):

	model = MetadataCategory

	# context_object_name = 'metadata_category_list'

	template_name = 'response_metadata/metadata_category_list.html'

	login_url = '/console/login/'

	def get_context_data(self,**kwargs):

		context = super(MetadataCategoryListView,self).get_context_data(**kwargs)

		context['all_metadata_category_list'] = MetadataCategory.objects.filter(company__in = self.request.user.company.all())
		context['data_category_list'] = MetadataCategory.objects.filter(company__in = self.request.user.company.all(),category_type__iexact='data')
		context['source_data_category_list'] = MetadataCategory.objects.filter(company__in = self.request.user.company.all(),category_type__iexact='source')
		context['vendor_category_list'] = MetadataCategory.objects.filter(company__in = self.request.user.company.all(),category_type__iexact='vendor')




		return context

class MetadataCategoryDetailView(LoginRequiredMixin,DetailView):
	model = MetadataCategory
	template_name = 'response_metadata/metadata_category_detail.html'

	login_url = '/console/login/'


class MetadataCategoryCreateView(LoginRequiredMixin,CreateView):
	model = MetadataCategory
	form_class = MetadataCategoryForm
	template_name = 'response_metadata/metadata_category_form.html'

	login_url = '/console/login/'

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)


class MetadataCategoryUpdateView(LoginRequiredMixin,UpdateView):
	model = MetadataCategory
	form_class = MetadataCategoryForm
	template_name = 'response_metadata/metadata_category_form.html'

	login_url = '/console/login/'

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)