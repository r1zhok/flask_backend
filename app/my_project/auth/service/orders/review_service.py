from my_project.auth.dao.orders import review_dao
from my_project.auth.service.general_service import GeneralService


class ReviewService(GeneralService):
    _dao = review_dao.ReviewDAO()

    def get_person_reviews(self, person_id):
        return self._dao.get_person_rating(person_id)
