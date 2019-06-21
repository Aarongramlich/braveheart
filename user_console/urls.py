from django.urls import path
from django.contrib.auth import views as auth_views
from user_console import views

from django.urls import reverse,reverse_lazy

app_name = 'user_console'

urlpatterns = [
	path('login/',auth_views.LoginView.as_view(template_name="user_console/login.html"),name='login'),
	path('change-password/',auth_views.PasswordChangeView.as_view(template_name="user_console/change-password.html"),name='change_password'),
	path('logged-out/',auth_views.LogoutView.as_view(template_name='user_console/logged_out.html'),name='logged_out'),

	path('home/',views.HomepageView.as_view(),name='home'),
	
	path('requests/',views.RequestListView.as_view(),name='request_list'),
	path('request/<int:pk>/',views.RequestDetailView.as_view(),name='request_detail'),
	path('request/<int:pk>/edit',views.RequestUpdate.as_view(),name='request_update'),
	path('request/create/',views.RequestCreateView.as_view(),name='request_create'),
	path('requests/export-all/',views.RequestExport,name='export_all_requests'),
	path('requests/import/',views.RequestImport,name='import_requests'),

	path('consumers/',views.ConsumerListView.as_view(),name='consumer_list'),
	path('consumer/create/',views.ConsumerCreateView.as_view(),name='consumer_create'),
	path('consumer/<int:pk>/',views.ConsumerDetailView.as_view(),name='consumer_detail'),
	path('consumer/<int:pk>/edit',views.ConsumerUpdate.as_view(),name='consumer_update'),

	path('companies/',views.CompanyListView.as_view(),name='company_list'),
	path('company/<int:pk>/',views.CompanyDetailView.as_view(),name='company_detail'),
	path('company/create/',views.CompanyCreateView.as_view(),name='company_create'),
	
	




	path('mycompany/',views.MyCompanyDetail.as_view(),name='my_company_detail'),
] 