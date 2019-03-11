from django.shortcuts import render
from . import models
from django.views.generic import (View, TemplateView, ListView, DetailView, 
									CreateView,DeleteView,UpdateView)
from django.urls import reverse, reverse_lazy

# Create your views here.

class IndexView(TemplateView):
	template_name = 'index.html'
