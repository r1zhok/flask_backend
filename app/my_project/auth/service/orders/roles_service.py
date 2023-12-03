from my_project.auth.dao.orders import roles_dao
from my_project.auth.service.general_service import GeneralService


class RolesService(GeneralService):
    _dao = roles_dao.RolesDAO()
