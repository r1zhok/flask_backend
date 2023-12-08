from my_project.auth.service.orders import rating_service
from my_project.auth.controller.general_controller import GeneralController


class RatingController(GeneralController):
    """
    Realisation of Rating controller.
    """
    _service = rating_service.RatingService()

    def get_person_rating(self, person_id: int):
        return list(map(lambda x: x.put_into_dto(), self._service.get_person_rating(person_id)))
