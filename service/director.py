from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, aid):
        return self.dao.get_one(aid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        aid = data.get("id")
        director = self.dao.get_one(aid)
        director.name = data.get("name")

        self.dao.update(director)

    def update_partial(self, data):
        aid = data.get("id")
        director = self.dao.get_one(aid)
        if "name" in data:
            director.title = data.get("name")

        self.dao.update(director)

    def delete(self, aid):
        self.dao.delete(aid)
