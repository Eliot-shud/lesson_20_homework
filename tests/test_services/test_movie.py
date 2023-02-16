import pytest

from service.movie import MovieService


class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie.id is not None
        assert movie.title is not None
        assert movie.id == 1
        assert movie.title == 'First movie'

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies is not None
        assert len(movies) > 0

    def test_create(self):
        dict_movie = {
            'id': 1,
            'title': 'First movie',
            'description': 'Description',
            'trailer': 'link',
            'year': 2022,
            'rating': 8.6,
            'genre_id': 1,
            'director_id': 1}

        new_movie = self.movie_service.create(dict_movie)
        assert new_movie.id is not None

    def test_update(self):
        dict_movie = {
            'id': 2,
            'title': 'Second movie',
            'description': 'Description',
            'trailer': 'link',
            'year': 2003,
            'rating': 8.9,
            'genre_id': 1,
            'director_id': 1}


        update_movie = self.movie_service.update(dict_movie)
        assert update_movie is not None

    def test_delete(self):
        assert self.movie_service.delete(1) is None
