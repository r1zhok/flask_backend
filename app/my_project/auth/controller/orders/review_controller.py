from my_project.auth.service.orders import review_service
from my_project.auth.controller.general_controller import GeneralController


class ReviewController(GeneralController):
    """
    Realisation of Review controller.
    """
    _service = review_service.ReviewService()

    def get_person_reviews(self, person_id):
        return list(map(lambda x: x.put_into_dto(), self._service.get_person_reviews(person_id)))
