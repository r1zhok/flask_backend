from my_project.auth.service.orders import extra_info_service
from my_project.auth.controller.general_controller import GeneralController


class ExtraInfoController(GeneralController):
    """
    Realisation of ExtraInfo controller.
    """
    _service = extra_info_service.ExtraInfoService()
