import pytest

from service.director import DirectorService


class TestDirectorService:

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.name is not None
        assert director.id == 1
        assert director.name == 'Director 1'

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert directors is not None
        assert len(directors) > 0

    def test_create(self):
        dict_director = {'name': 'Director 1'}
        new_director = self.director_service.create(dict_director)
        print(new_director)
        assert new_director.id is not None

    def test_update(self):
        dict_director = {'name': 'Director 2'}
        update_director = self.director_service.update(dict_director)
        assert update_director is not None

    def test_delete(self):
        assert self.director_service.delete(1) is None

