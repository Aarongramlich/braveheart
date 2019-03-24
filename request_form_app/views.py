from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from .forms import ConsumerBasicInfoForm
from django.views.generic import (View, TemplateView, ListView, DetailView, 
									CreateView,DeleteView,UpdateView)
from django.urls import reverse, reverse_lazy

# Create your views here.

# def ConsumerBasicInfoView(request):
# 	if request.method == 'POST':
# 		form = ConsumerBasicInfoForm(request.POST)
# 		if form.is_valid():
# 			return HttpResponseRedirect('/thanks/')
# 	else:
# 		form = ConsumerBasicInfoForm(request.POST)

# 	return render(request,'basic_info_form.html', {'form': form})

def ConsumerBasicInfoView(request):
	if request.method == 'POST':
		form = ConsumerBasicInfoForm()
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = ConsumerBasicInfoForm(request.POST)

	return render(request,'request_form_app/basic_info_form.html', {'form': form})

class IndexView(TemplateView):
	template_name = 'index.html'