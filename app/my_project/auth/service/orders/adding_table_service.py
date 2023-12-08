from my_project.auth.dao.orders import adding_table_dao
from my_project.auth.service.general_service import GeneralService


class AddingTableService(GeneralService):
    _dao = adding_table_dao.AddingTableDAO()