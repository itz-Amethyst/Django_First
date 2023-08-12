from django.http import HttpResponse , HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
days = {
	"saturday": "Today is saturday",
	"sunday": "Today is Sunday",
	"monday": "Today is Monday",
	"tuesday": "Today is Tuesday",
	"wednesday": "Today is Wednesday",
	"thursday": "Today is Thursday",
	"friday": "Today is Friday",
}



def index(request):
	return HttpResponse("this is a response from index")

def sunday(request):
	return HttpResponse("this is a response from sunday")

def dynamic_days(request , day):
	day_data = days.get(day.lower())
	if day_data is not None:
		return HttpResponse(f"The data i found is : {day_data}")
	return HttpResponseNotFound("day does not exist")
