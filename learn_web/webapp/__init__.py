from flask import Flask, render_template

from learn_python.learn_web.webapp.weather import weather_by_city
from learn_python.learn_web.webapp.python_org_news import get_python_news


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        page_title = "Новости Python"
        weather = weather_by_city("Moscow, Russia")
        news_list = get_python_news()
        return render_template('index.html', page_title=page_title,
                              weather=weather, news_list=news_list)
    return app
