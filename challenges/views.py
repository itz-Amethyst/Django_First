from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

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

def days_list(request):
	days_list = list(days.keys())
	list_items = ""

	for day in days_list:
		url_path = reverse('days-of-week', args = [day])
		list_items += f'<li> <a href="{url_path}"> {day} </a> </li> \n'

	content = f'<ul>\n {list_items} \n</ul>'

	return HttpResponse(content)

# def index(request):
# 	return HttpResponse("this is a response from index")

# def sunday(request):
# 	return HttpResponse("this is a response from sunday")

def dynamic_days_by_number(request, day):
	days_name = list(days.keys())
	if day > len(days_name):
		return HttpResponse('day does not exists')
	redirect_day = days_name[day - 1]
	redirect_url = reverse('days-of-week', args = [redirect_day])
	return HttpResponseRedirect(redirect_url)


def dynamic_days(request , day):
	day_data = days.get(day.lower())
	if day_data is not None:
		data = {
			"Rango" : day_data
		}
		#DTL -> Django Template Language

		return render(request, 'challenges/index.html' , data)
		# response = render_to_string('challenges/index.html')
		# return HttpResponse(response)
	return HttpResponseNotFound("day does not exist")
