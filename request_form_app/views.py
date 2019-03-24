from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms
from django.views.generic import (View, TemplateView, ListView, DetailView, 
									CreateView,DeleteView,UpdateView)
from django.urls import reverse, reverse_lazy

# Create your views here.

def ConsumerBasicInfoForm(request):
	if request.method == 'POST':
		form = ConsumerBasicInfoForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = ConsumerBasicInfoForm()

	return render(request,'basic_info_form.html', {'form': form})

class IndexView(TemplateView):
	template_name = 'index.html'