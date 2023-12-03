from my_project.auth.dao.orders import genre_dao
from my_project.auth.service.general_service import GeneralService


class GenreService(GeneralService):
    _dao = genre_dao.GenreDAO()
