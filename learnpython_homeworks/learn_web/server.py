from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    weather = weather_by_city("Moscow, Russia")
    if weather:
        weather_text = f"Погода: {weather['temp_C']} " \
               f"Ощущается как: {weather['FeelsLikeC']}"
    else:
        weather_text = "Сервис погоды временно не доступен"
    return f"""
    <html>
        <head>
            <title>Прогноз погоды</title>  
        </head>
        <body>
            <h1>{weather_text}</h1>
            <ol>
                <li>Один</li>
                <li>Два</li>
                <li>Три</li> 
            </ol>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
