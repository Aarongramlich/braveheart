from django.urls import path
from django.contrib.auth import views as auth_views
from response_metadata import views

from django.urls import reverse,reverse_lazy

app_name = 'response_metadata'

urlpatterns = [
	path('',views.MetadataListView.as_view(),name='metadata_list'),
	path('<str:pk>/',views.MetadataDetailView.as_view(),name='metadata_detail'),
]