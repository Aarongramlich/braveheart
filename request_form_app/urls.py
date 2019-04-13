from django.urls import path
from request_form_app import views

app_name = 'request_form_app'

urlpatterns = [
	path('',views.CaseCreateView.as_view(),name='case_create'),
	path('<int:pk>/',views.CaseDetailView.as_view(),name='case_detail')
]