from django.urls import path
from django.contrib.auth import views as auth_views
from response_metadata import views

from django.urls import reverse,reverse_lazy

app_name = 'response_metadata'

urlpatterns = [
	path('data/',views.MetadataListView.as_view(),name='metadata_list'),
	path('data/create/',views.MetadataCreateView.as_view(),name='metadata_create'),
	path('data/<str:pk>/',views.MetadataDetailView.as_view(),name='metadata_detail'),
	path('data/<str:pk>/update/',views.MetadataUpdateView.as_view(),name='metadata_update'),

	
	path('category/',views.MetadataCategoryListView.as_view(),name='metadata_category_list'),
	path('category/create/',views.MetadataCategoryCreateView.as_view(),name='metadata_category_create'),
	path('category/<int:pk>/',views.MetadataCategoryDetailView.as_view(),name='metadata_category_detail'),
	path('category/<int:pk>/update/',views.MetadataCategoryUpdateView.as_view(),name='metadata_category_update'),

]