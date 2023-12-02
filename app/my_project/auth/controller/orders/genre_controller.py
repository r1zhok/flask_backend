from my_project.auth.service.orders import genre_service
from my_project.auth.controller.general_controller import GeneralController


class GenreController(GeneralController):
    """
    Realisation of Genre controller.
    """
    _service = genre_service.GenreService()
