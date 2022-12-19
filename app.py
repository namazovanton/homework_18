# Основной файл приложения.
# Здесь конфигурируется фласк, сервисы, SQLAlchemy
# и все остальное что требуется для приложения.
# Этот файл часто является точкой входа в приложение

# Пример
# from flask import Flask
# from flask_restx import Api
#
# from config import Config
# from models import Review, Book
# from setup_db import db
# from views.books import book_ns
# from views.reviews import review_ns
#
# функция создания основного объекта app
# def create_app(config_object):
#     app = Flask(__name__)
#     app.config.from_object(config_object)
#     register_extensions(app)
#     return app
#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
# def register_extensions(app):
#     db.init_app(app)
#     api = Api(app)
#     api.add_namespace(...)
#     create_data(app, db)
#
#
# функция
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#
#
# app = create_app(Config())
# app.debug = True
#
# if __name__ == '__main__':
#     app.run(host="localhost", port=10001, debug=True)

from flask import Flask
from flask_restx import Api
from config import Config
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from setup_db import db
from views.directors import directors_ns
from views.genres import genres_ns
from views.movies import movies_ns


# Создаем приложение Flask
def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


if __name__ == "__main__":
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.run()
