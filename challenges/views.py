from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
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

def dynamic_days_by_number(request, day):
	days_name = list(days.keys())
	if day > len(days_name):
		return HttpResponse('day does not exists')
	redirect_day = days_name[day - 1]
	return HttpResponseRedirect(f'/days/{redirect_day}')


def dynamic_days(request , day):
	day_data = days.get(day.lower())
	if day_data is not None:
		return HttpResponse(f"The data i found is : {day_data}")
	return HttpResponseNotFound("day does not exist")
