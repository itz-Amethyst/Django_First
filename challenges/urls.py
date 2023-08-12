from django.urls import path

from . import  views

urlpatterns = [
	path('index', views.index),
	path('sunday', views.sunday),
	path('<day>', views.dynamic_days)
]