import pytest
from unittest.mock import MagicMock
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name='Александр')
    d2 = Director(id=2, name='Валера')

    data_dict = {
        1: d1,
        2: d2
    }

    director_dao.get_one = MagicMock(return_value=data_dict.get(1))
    director_dao.get_all = MagicMock(return_value=data_dict.values())
    director_dao.create = MagicMock(return_value=data_dict.get(1))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name="Фантастика")
    g2 = Genre(id=2, name='Драма')

    data_dict = {
        1: g1,
        2: g2
    }

    genre_dao.get_one = MagicMock(return_value=data_dict.get(1))
    genre_dao.get_all = MagicMock(return_value=data_dict.values())
    genre_dao.create = MagicMock(return_value=data_dict.get(1))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title='First film', description='text', trailer='link',
               year=2018, rating=8.6, genre_id=1, director_id=1)

    m2 = Movie(id=2, title='Second film', description='text', trailer='link',
               year=2018, rating=8.6, genre_id=1, director_id=1)

    data_dict = {
        1: m1,
        2: m2
    }

    movie_dao.get_one = MagicMock(return_value=data_dict.get(1))
    movie_dao.get_all = MagicMock(return_value=data_dict.values())
    movie_dao.create = MagicMock(return_value=data_dict.get(1))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
