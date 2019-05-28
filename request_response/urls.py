from django.urls import path
from django.contrib.auth import views as auth_views
from .views import GeneratePdf

from django.urls import reverse,reverse_lazy

app_name = 'request_response'

urlpatterns = [
	path('pdf/<int:pk>/',GeneratePdf.as_view(),name='pdf'),
]