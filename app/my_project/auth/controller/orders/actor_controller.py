from my_project.auth.service.orders import actor_service
from my_project.auth.controller.general_controller import GeneralController


class ActorController(GeneralController):
    """
    Realisation of Actor controller.
    """
    _service = actor_service.ActorService()
