from flask import Flask, render_template
from flask_login import LoginManager, current_user, login_required

from .weather import weather_by_city
from .python_org_news import get_python_news
from .model import db, News
from .user.models import User
from .user.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        page_title = "Новости Python"
        weather = weather_by_city(app.config['WEATHER_SITY'])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=page_title,
                               weather=weather, news_list=news_list)

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Hi, Admin!'
        else:
            return 'You are not Admin!'

    return app
