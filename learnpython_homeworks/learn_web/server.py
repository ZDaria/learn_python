from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    weather = weather_by_city("Moscow, Russia")
    if weather:
        return f"Погода: {weather['temp_C']} " \
               f"Ощущается как: {weather['FeelsLikeC']}"
    else:
        return "Сервис погоды временно не доступен"


if __name__ == "__main__":
    app.run(debug=True)
