import csv
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import View,TemplateView,ListView,DetailView,FormView,UpdateView,CreateView
from django.http import HttpResponse, HttpResponseRedirect

from response_metadata.models import Metadata

from accounts.models import User

from request_response import urls

from response_metadata.forms import MetadataForm
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_list_or_404,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from tablib import Dataset
from datetime import date,timedelta,datetime,timezone


# Create your views here.

class MetadataListView(LoginRequiredMixin,ListView):
	model = Metadata

	context_object_name = 'metadata_list'
	template_name='response_metadata/metadata_list.html'

	login_url = '/console/login/'

	def get_context_data(self,**kwargs):

		context = super(MetadataListView,self).get_context_data(**kwargs)
		context['all_metadata_list'] = Metadata.objects.filter(company__in = self.request.user.company.all())
		context['personal_meta_list']= Metadata.objects.filter(data_category__iexact='personal',company__in = self.request.user.company.all())
		context['commercial_meta_list']= Metadata.objects.filter(data_category__iexact='commercial',company__in = self.request.user.company.all())
		context['biometric_meta_list']= Metadata.objects.filter(data_category__iexact='biometric',company__in = self.request.user.company.all())
		context['internet_meta_list']= Metadata.objects.filter(data_category__iexact='internet',company__in = self.request.user.company.all())
		context['geolocation_meta_list']= Metadata.objects.filter(data_category__iexact='geolocation',company__in = self.request.user.company.all())
		context['sensory_meta_list']= Metadata.objects.filter(data_category__iexact='sensory',company__in = self.request.user.company.all())
		context['psychometric_meta_list']= Metadata.objects.filter(data_category__iexact='psychometric',company__in = self.request.user.company.all())
		context['employment_meta_list']= Metadata.objects.filter(data_category__iexact='employment',company__in = self.request.user.company.all())
		context['inferred_meta_list']= Metadata.objects.filter(data_category__iexact='inferred',company__in = self.request.user.company.all())
		return context



class MetadataDetailView(LoginRequiredMixin,DetailView):
	model = Metadata
	template_name = 'response_metadata/metadata_detail.html'

	login_url = '/console/login/'