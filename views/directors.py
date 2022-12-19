from flask import request
from flask_restx import Resource, Namespace

from implemented import director_service
from dao.model.director import DirectorSchema

directors_ns = Namespace('directors')

director_schema = DirectorSchema()  # В единственном экземпляре
directors_schema = DirectorSchema(many=True)  # Множество экземпляров


@directors_ns.route('/')  # /directors/
class DirectorsView(Resource):
    def get(self):  # Получение данных
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    def post(self):  # Добавление данных
        red_json = request.json
        director_service.create(red_json)
        return "Director created", 201


@directors_ns.route('/<int:uid>')  # /directors/<int:uid>
class DirectorView(Resource):
    def get(self, uid: int):  # Получение данных
        try:
            director = director_service.get_one(uid)
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404

    def put(self, uid: int):  # Замена данных
        red_json = request.json
        red_json["id"] = uid
        director_service.update(red_json)
        return "Director updated", 204

    def patch(self, uid: int):  # Частичное обновление данных
        red_json = request.json
        red_json["id"] = uid
        director_service.update_partial(red_json)
        return "Director updated", 204

    def delete(self, uid: int):  # Удаление данных
        director_service.delete(uid)
        return "Director deleted", 204
