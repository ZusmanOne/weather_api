from flask import jsonify, request, redirect, url_for
import requests
from core import app
from core import cache


API_KEY = app.config.get("API_KEY")

@app.route('/weather/<city>')
def get_city_coordinates(city):
    url_city = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}'
    response = requests.get(url_city)
    city_serializer = response.json()
    lat = city_serializer[0]['lat']
    lon = city_serializer[0]['lon']
    return redirect(url_for('get_weather', lat=lat, lon=lon))


@app.route('/', methods=['GET'])
@cache.cached(timeout=1800, query_string=True)
def get_weather():
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    response = requests.get(weather_url, params={'lat': lat,
                                  'lon': lon,
                                  'appid': API_KEY,
                                  'units': 'metric'})
    json_string = response.json()
    location_temp = json_string['main']['temp']
    location_pressure = json_string['main']['pressure'] // 1.333
    wind_speed = json_string['wind']['speed']
    weather_data = {'air temperature': f'{location_temp} c',
                    'atmospheric pressure': f'{location_pressure} mm Hg',
                    'wind speed': f'{wind_speed} m/s'}
    return jsonify(weather_data)
