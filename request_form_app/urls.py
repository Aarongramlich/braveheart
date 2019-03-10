 from django.urls import path
 from request_form_app import views

 app_name = 'request_form_app'

 urlpatterns = [
 	path('request/',views.IndexView(),name='step one'),
 ]