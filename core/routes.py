from flask import jsonify, request, redirect, url_for
import requests
from core import app
from core import cache


@app.route('/weather/<city>')
def get_city_coordinates(city):
    url_city = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={app.config.get("API_KEY")}'
    response = requests.get(url_city)
    city_serializer = response.json()
    lat = city_serializer[0]['lat']
    lon = city_serializer[0]['lon']
    return redirect(url_for('get_weather', lat=lat, lon=lon))


@app.route('/', methods=['GET'])
@cache.cached(timeout=1800, query_string=True)
def get_weather():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    search1 = request.args.get('lat')
    search2 = request.args.get('lon')
    search3 = app.config.get("API_KEY")
    r = requests.get(url, params={'lat': search1,
                                  'lon': search2,
                                  'appid': search3,
                                  'units': 'metric'})
    my_json = r.json()
    location_temp = my_json['main']['temp']
    location_pressure = my_json['main']['pressure'] // 1.333
    wind_speed = my_json['wind']['speed']
    weather_data = {'air temperature': f'{location_temp} c',
                    'atmospheric pressure': f'{location_pressure} mm Hg',
                    'wind speed': f'{wind_speed} m/s'}
    return jsonify(weather_data)
