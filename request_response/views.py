import csv,io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import View,TemplateView,ListView,DetailView,FormView,UpdateView,CreateView
from django.contrib.auth.decorators import permission_required 

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ResponseData,RequestResponse


# Create your views here.

@permission_required('admin.admin')
def request_response_upload(request)
	template = "request_response_upload.html"