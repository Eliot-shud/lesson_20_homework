import pytest
from unittest.mock import MagicMock

from setup_db import db
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO


# фикстура для directorDAO
@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(db.session)

    d1 = Director(id=1, name='Director 1')
    d2 = Director(id=2, name='Director 2')
    d3 = Director(id=2, name='Director 3')

    directors = {
        1: d1,
        2: d2,
        3: d3
    }

    director_dao.get_one = MagicMock(return_value=directors.get(1))
    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.create = MagicMock(return_value=directors.get(1))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


# фикстура для GenreDAO
@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(db.session)

    g1 = Genre(id=1, name="Фантастика")
    g2 = Genre(id=2, name='Драма')
    g3 = Genre(id=2, name='Комедия')

    genres = {
        1: g1,
        2: g2,
        3: g3
    }

    genre_dao.get_one = MagicMock(return_value=genres.get(1))
    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.create = MagicMock(return_value=genres.get(1))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


# фикстура для MovieDAO
@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(db.session)

    m1 = Movie(id=1, title='First movie', description='Description', trailer='link',
               year=2022, rating=8.6, genre_id=1, director_id=1)

    m2 = Movie(id=2, title='Second movie', description='Description', trailer='link',
               year=2003, rating=8.9, genre_id=1, director_id=1)

    m3 = Movie(id=3, title='Third movie', description='Description', trailer='link',
               year=2007, rating=9.4, genre_id=1, director_id=1)

    movies = {
        1: m1,
        2: m2,
        3: m3
    }

    movie_dao.get_one = MagicMock(return_value=movies.get(1))
    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.create = MagicMock(return_value=movies.get(1))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
