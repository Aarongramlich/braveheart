from django.urls import path
from django.contrib.auth import views as auth_views
from request_response import views

from django.urls import reverse,reverse_lazy

app_name = 'request_response'

urlpatterns = [
	# path('pdf/<int:pk>/',views.GeneratePdf.as_view(),name='pdf'),
	path('pdf/<int:pk>/',views.TestPdf.as_view(),name='pdf'),
	path('request-response/<int:pk>/',views.RequestResponseDetailView.as_view(),name='response_detail'),
	path('request-response/<int:pk>/udpate/',views.RequestResponseUpdateView.as_view(),name='response_update'),



	# path('request/response/<int:pk>/add/',views.request_response_upload,name='create_response'),
	path('request/<int:pk>/add/',views.RequestResponseCreateView.as_view(),name='create_response'),
	path('response-data/<int:pk>/',views.ResponseDataDetailView.as_view(),name='response_data_detail'),
	path('request/<int:pk>/response-data/add/',views.ResponseDataCreateView.as_view(),name='create_response_data'),
	path('response-data/<int:pk>/update',views.ResponseDataUpdateView.as_view(),name='response_data_update'),


	path('response-category/<int:pk>/',views.ResponseCategoryDetailView.as_view(),name='response_category_detail'),
	path('request/<int:pk>/response-category/add/',views.ResponseCategoryCreateView.as_view(),name='create_response_category'),
	path('request-category/<int:pk>/udpate/',views.RequestResponseUpdateView.as_view(),name='response_category_update'),


	path('response-data/import/',views.ResponseDataImport,name='import_response_data')
]