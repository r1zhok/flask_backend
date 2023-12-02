from my_project.auth.service.orders import description_service
from my_project.auth.controller.general_controller import GeneralController


class DescriptionController(GeneralController):
    """
    Realisation of Description controller.
    """
    _service = description_service.DescriptionService()
