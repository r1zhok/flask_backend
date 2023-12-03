from my_project.auth.dao.orders import film_has_rating_dao
from my_project.auth.service.general_service import GeneralService


class FilmHasRatingService(GeneralService):
    _dao = film_has_rating_dao.FilmHasRatingDAO()
