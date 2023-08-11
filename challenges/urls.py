from django.urls import path

from . import  views

urlpatterns = [
	path('index', views.index),
	path('edit_profile', views.edit_profile)
]