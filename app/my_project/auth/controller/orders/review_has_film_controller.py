from my_project.auth.service.orders import review_has_film_service
from my_project.auth.controller.general_controller import GeneralController


class ReviewHasFilmController(GeneralController):
    """
    Realisation of ReviewHasFilm controller.
    """
    _service = review_has_film_service.ReviewHasFilmService()
