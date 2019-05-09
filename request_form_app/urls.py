from django.urls import path
from request_form_app import views

app_name = 'request_form_app'

urlpatterns = [
	path('',views.RequestCreateView.as_view(),name='request_create'),
	path('<int:pk>/',views.RequestDetailView.as_view(),name='request_detail')
]