from my_project.auth.dao.orders import rating_dao
from my_project.auth.service.general_service import GeneralService


class RatingService(GeneralService):
    _dao = rating_dao.RatingDAO()
