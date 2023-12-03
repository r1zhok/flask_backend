from my_project.auth.service.orders import rating_service
from my_project.auth.controller.general_controller import GeneralController


class RatingController(GeneralController):
    """
    Realisation of Rating controller.
    """
    _service = rating_service.RatingService()
