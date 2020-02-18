from django.shortcuts import render, redirect
import requests
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'az_AZ')

# Create your views here.


def weatherView(request):
    if request.method == 'POST':
        city = request.POST['city']
    else:
        city = 'Baku'
    try: # 5day api key used
        url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=e1b5f47f4c753f0fcf6b047f6b635121'
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city,
            'country': r['city']['country'],
            'pressure': int(r['list'][0]['main']['pressure'] * 0.75006),
            'description': r['list'][0]['weather'][0]['description'],
            'temperature1': round(r['list'][0]['main']['temp'], 1),
            'temperature2': round(r['list'][8]['main']['temp'], 1),
            'temperature3': round(r['list'][16]['main']['temp'], 1),
            'temperature4': round(r['list'][24]['main']['temp'], 1),
            'temperature5': round(r['list'][32]['main']['temp'], 1),
            'icon0': r['list'][0]['weather'][0]['icon'],
            'icon1': r['list'][6]['weather'][0]['icon'],
            'icon2': r['list'][16]['weather'][0]['icon'],
            'icon3': r['list'][24]['weather'][0]['icon'],
            'icon4': r['list'][32]['weather'][0]['icon'],
            'icon5': r['list'][0]['weather'][0]['icon'],
            'icon6': r['list'][6]['weather'][0]['icon'],
            'clouds': r['list'][0]['clouds']['all'],
            'wind': r['list'][0]['wind']['speed'],
            'wind_dir': r['list'][0]['wind'].get('deg', 'not info'),
            'main': r['list'][0]['weather'][0]['main'],
            'weekday1': datetime.strftime(datetime.now(), '%A').title(),
            'weekday2': datetime.strftime(datetime.fromtimestamp(r['list'][8]['dt']), '%A').title(),
            'weekday3': datetime.strftime(datetime.fromtimestamp(r['list'][16]['dt']), '%A').title(),
            'weekday4': datetime.strftime(datetime.fromtimestamp(r['list'][24]['dt']), '%A').title(),
            'weekday5': datetime.strftime(datetime.fromtimestamp(r['list'][32]['dt']), '%A').title(),
            'date': datetime.now(),
            'humidity': r['list'][0]['main']['humidity'],
            }
        
        context = {
            'city_weather': city_weather,
            }
    except:
        return redirect('weather')
    return render(request, 'weather.html', context)

