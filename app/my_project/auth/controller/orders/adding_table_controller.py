from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import adding_table_service


class AddingTableController(GeneralController):
    _service = adding_table_service.AddingTableService()
