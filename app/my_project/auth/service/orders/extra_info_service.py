from my_project.auth.dao.orders import extra_info_dao
from my_project.auth.service.general_service import GeneralService


class ExtraInfoService(GeneralService):
    _dao = extra_info_dao.ExtraInfoDAO()
