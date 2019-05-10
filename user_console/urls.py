from django.urls import path
from django.contrib.auth import views as auth_views
from user_console import views

app_name = 'user_console'

urlpatterns = [
	path('login/',auth_views.LoginView.as_view(template_name="user_console/login.html"),name='login'),
	path('change-password/',auth_views.PasswordChangeView.as_view(template_name="user_console/change-password.html"),name='change_password'),
	path('home/',views.HomepageView.as_view(),name='home'),
	path('logged-out/',auth_views.LogoutView.as_view(template_name='user_console/logged_out.html'),name='logged_out'),
	path('requests/',views.RequestListView.as_view(),name='request_list'),
	path('request/<int:pk>/',views.RequestDetailView.as_view(),name='request_detail'),
	path('consumers/',views.ConsumerListView.as_view(),name='consumer_list'),
	path('companies/',views.CompanyListView.as_view(),name='company_list'),
	path('request/<int:pk>/edit',views.RequestUpdate.as_view(),name='request_update')
]