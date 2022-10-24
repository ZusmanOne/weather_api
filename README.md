# Сервис получения погоды 
Cервис интегрируется с API [сайта](https://openweathermap.org/)

## Описание задания

- Реализовать API, которое на HTTP-запрос GET /weather/<city_name>, 
  где <city_name> - это название города на английском языке, 
  возвращает текущую температуру в этом городе в градусах Цельсия, 
  атомсферное давление (мм рт.ст.) и скорость ветра (м/c).

### Как запустить dev-версию 
Скачайте код:
```sh
git clone https://github.com/ZusmanOne/weather_api.git
```

Перейдите в каталог проекта:
```sh
cd weather_api
```
[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`

Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```
Настройка: создать файл `.env` в каталоге `payment_project/` со следующими настройками:

-`CACHE_TYPE`=redis
-`CACHE_REDIS_HOST`=redis
-`CACHE_REDIS_PORT`=6379
-`CACHE_REDIS_DB`=0
-`CACHE_REDIS_URL`=redis://localhost:6379/0
-`CACHE_DEFAULT_TIMEOUT`=500
-`FLASK_DEBUG`=True
-`API_KEY`- получите api ключ при регистрации на [сайте](https://openweathermap.org/)

Настройка: создать файл `.flaskenv` в каталоге `payment_project/` со следующими настройками:
-`FLASK_APP`=app

Запустить сервер
```sh
flask run
```

Сервис имеют следующую маршрутизацию



```http://127.0.0.1:5000/weather/<city>/``` - получит координаты города и перенаправит на результат погоды



