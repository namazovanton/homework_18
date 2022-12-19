from flask import request
from flask_restx import Resource, Namespace

from implemented import genre_service
from dao.model.genre import GenreSchema

genres_ns = Namespace('genres')

genre_schema = GenreSchema()  # В единственном экземпляре
genres_schema = GenreSchema(many=True)  # Множество экземпляров


@genres_ns.route('/')  # /genres/
class GenresView(Resource):
    def get(self):  # Получение данных
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    def post(self):  # Добавление данных
        red_json = request.json
        genre_service.create(red_json)
        return "Genre created", 201


@genres_ns.route('/<int:uid>')  # /genres/<int:uid>
class GenreView(Resource):
    def get(self, uid: int):  # Получение данных
        try:
            # Получение данных из БД по ID
            genre = genre_service.get_one(uid)
            # Сериализация данных
            return genre_schema.dump(genre), 200
        # Ошибка в случае если в базе нет жанра по ID из запроса
        except Exception as e:
            return str(e), 404

    def put(self, uid: int):  # Замена данных
        red_json = request.json
        red_json["id"] = uid
        genre_service.update(red_json)
        return "Genre updated", 204

    def patch(self, uid: int):  # Частичное обновление данных
        red_json = request.json
        red_json["id"] = uid
        genre_service.update_partial(red_json)
        return "Genre updated", 204

    def delete(self, uid: int):  # Удаление данных
        genre_service.delete(uid)
        return "Genre deleted", 204
