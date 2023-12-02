from my_project.auth.dao.orders import person_dao
from my_project.auth.service.general_service import GeneralService


class PersonService(GeneralService):
    _dao = person_dao.PersonDAO()
