from my_project.auth.service.orders import film_service
from my_project.auth.controller.general_controller import GeneralController


class FilmController(GeneralController):
    """
    Realisation of Film controller.
    """
    _service = film_service.FilmService()
