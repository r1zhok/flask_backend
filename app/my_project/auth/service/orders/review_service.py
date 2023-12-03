from my_project.auth.dao.orders import review_dao
from my_project.auth.service.general_service import GeneralService


class ReviewService(GeneralService):
    _dao = review_dao.ReviewDAO()
