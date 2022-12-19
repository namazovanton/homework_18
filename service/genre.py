from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, aid):
        return self.dao.get_one(aid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        aid = data.get("id")
        genre = self.dao.get_one(aid)
        genre.name = data.get("name")

        self.dao.update(genre)

    def update_partial(self, data):
        aid = data.get("id")
        genre = self.dao.get_one(aid)
        if "name" in data:
            genre.title = data.get("name")

        self.dao.update(genre)

    def delete(self, aid):
        self.dao.delete(aid)
