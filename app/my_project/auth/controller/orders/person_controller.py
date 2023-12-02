from my_project.auth.service.orders import person_service
from my_project.auth.controller.general_controller import GeneralController


class PersonController(GeneralController):
    """
    Realisation of Person controller.
    """
    _service = person_service.PersonService()
