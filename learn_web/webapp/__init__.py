from flask import Flask, render_template

from .weather import weather_by_city
from .python_org_news import get_python_news
from .model import db, News


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    @app.route('/')
    def index():
        page_title = "Новости Python"
        weather = weather_by_city(app.config['WEATHER_SITY'])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=page_title,
                              weather=weather, news_list=news_list)

    return app
