from my_project.auth.service.orders import review_service
from my_project.auth.controller.general_controller import GeneralController


class ReviewController(GeneralController):
    """
    Realisation of Review controller.
    """
    _service = review_service.ReviewService()
