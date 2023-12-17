from my_project.auth.dao.orders import film_has_rating_dao
from my_project.auth.service.general_service import GeneralService


class FilmHasRatingService(GeneralService):
    _dao = film_has_rating_dao.FilmHasRatingDAO()

    def insert_data_procedure(self, p_name: str, mark: int, person_id):
        self._dao.insert_data_procedure(p_name, mark, person_id)
