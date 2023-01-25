import pytest

from service.genre import GenreService


class TestGenreService:

    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre.id is not None
        assert genre.name is not None
        assert genre.id == 1
        assert genre.name == 'Фантастика'

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert genres is not None
        assert len(genres) > 0

    def test_create(self):
        dict_genre = {'name': 'Ужасы'}
        new_genre = self.genre_service.create(dict_genre)
        assert new_genre.id is not None

    def test_update(self):
        dict_director = {'name': 'Комедия'}
        update_director = self.genre_service.update(dict_director)
        assert update_director is not None

    def test_delete(self):
        assert self.genre_service.delete(1) is None
