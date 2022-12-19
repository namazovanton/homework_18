from dao.model.movie import Movie
from flask import request


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, aid):
        return self.session.query(Movie).get(aid)

    def get_all(self):
        movie_query = self.session.query(Movie).all()
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")
        if director_id is not None:
            movie_query = self.session.query(Movie).filter(Movie.director_id == director_id)
        if genre_id is not None:
            movie_query = self.session.query(Movie).filter(Movie.genre_id == genre_id)
        if year is not None:
            movie_query = self.session.query(Movie).filter(Movie.year == year)
        return movie_query

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, aid):
        movie = self.get_one(aid)
        self.session.delete(movie)
        self.session.commit()
