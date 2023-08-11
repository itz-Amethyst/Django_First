from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	return HttpResponse("this is a response from index")

def edit_profile(request):
	return HttpResponse("this is a response from edit-profile")