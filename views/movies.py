from flask import request
from flask_restx import Resource, Namespace

from implemented import movie_service
from dao.model.movie import MovieSchema

movies_ns = Namespace('movies')

movie_schema = MovieSchema()  # В единственном экземпляре
movies_schema = MovieSchema(many=True)  # Множество экземпляров


@movies_ns.route('/')  # /movies/
class MoviesView(Resource):
    def get(self):  # Получение данных
        movie_query = movie_service.get_all()
        return movies_schema.dump(movie_query), 200

    def post(self):  # Добавление данных
        red_json = request.json
        movie_service.create(red_json)
        return "Movie created", 201


@movies_ns.route('/<int:uid>')  # /movies/<int:id>
class MovieView(Resource):
    def get(self, uid: int):  # Получение данных
        try:
            movie = movie_service.get_one(uid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404

    def put(self, uid):  # Замена данных
        red_json = request.json
        red_json["id"] = uid
        movie_service.update(red_json)
        return "Movie updated", 204

    def patch(self, uid):  # Частичное обновление данных
        red_json = request.json
        red_json["id"] = uid
        movie_service.update_partial(red_json)
        return "Movie updated", 204

    def delete(self, uid: int):  # Удаление данных
        movie_service.delete(uid)
        return "Movie deleted", 204
