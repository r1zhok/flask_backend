from my_project.auth.service.orders import film_has_rating_service
from my_project.auth.controller.general_controller import GeneralController


class FilmHasRatingController(GeneralController):
    """
    Realisation of FilmHasRating controller.
    """
    _service = film_has_rating_service.FilmHasRatingService()

    def insert_data_procedure(self, p_name: str, mark: int):
        self._service.insert_data_procedure(p_name, mark)
