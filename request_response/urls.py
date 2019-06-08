from django.urls import path
from django.contrib.auth import views as auth_views
from request_response import views

from django.urls import reverse,reverse_lazy

app_name = 'request_response'

urlpatterns = [
	path('pdf/<int:pk>/',views.GeneratePdf.as_view(),name='pdf'),
	path('request/<int:pk>/',views.RequestResponseDetailView.as_view(),name='response_detail'),
	# path('request/response/<int:pk>/add/',views.request_response_upload,name='create_response'),
	path('request/<int:pk>/add/',views.RequestResponseCreateView.as_view(),name='create_response'),
	path('response-data/<int:pk>/',views.ResponseDataDetailView.as_view(),name='response_data_detail'),
	path('request/<int:pk>/response-data/add/',views.ResponseDataCreateView.as_view(),name='create_response_data'),
]