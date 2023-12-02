from my_project.auth.dao.orders import review_has_film_dao
from my_project.auth.service.general_service import GeneralService


class ReviewHasFilmService(GeneralService):
    _dao = review_has_film_dao.ReviewHasFilmDAO()
