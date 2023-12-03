from my_project.auth.service.orders import roles_service
from my_project.auth.controller.general_controller import GeneralController


class RolesController(GeneralController):
    """
    Realisation of Roles controller.
    """
    _service = roles_service.RolesService()
