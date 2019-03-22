from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def home(request):

	#url_zipcCode = 'api.openweathermap.org/data/2.5/weather?zip={},{}&245665885b07d0d9918e59d40ecc1a2d'
	url_cityName = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=245665885b07d0d9918e59d40ecc1a2d'

	if request.method == 'POST':
		print(request.POST)
		form = CityForm(request.POST)
		form.save()

	form = CityForm()

	cities = City.objects.all()	

	weather_data = []

	for city in cities:
		r = requests.get(url_cityName.format(city)).json()

		weather_dict = {
			'city': city.name,
			'temperature': r['main']['temp'],
			'description': r['weather'][0]['description'],
			'icon':r['weather'][0]['icon'],
		}
		weather_data.append(weather_dict)
	context = {'weather_data' : weather_data,'form':form}
	print(weather_dict)

	return render(request,'wheater_app/weather.html',context)
