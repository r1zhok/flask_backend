from my_project.auth.dao.orders import rating_dao
from my_project.auth.service.general_service import GeneralService


class RatingService(GeneralService):
    _dao = rating_dao.RatingDAO()

    def get_person_rating(self, person_id: int):
        return self._dao.get_person_rating(person_id)
