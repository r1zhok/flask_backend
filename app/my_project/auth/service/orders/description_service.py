from my_project.auth.dao.orders import description_dao
from my_project.auth.service.general_service import GeneralService


class DescriptionService(GeneralService):
    _dao = description_dao.DescriptionDAO()
