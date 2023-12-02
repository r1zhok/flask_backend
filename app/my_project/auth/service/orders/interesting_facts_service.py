from my_project.auth.dao.orders import interesting_facts_dao
from my_project.auth.service.general_service import GeneralService


class InterestingFactsService(GeneralService):
    _dao = interesting_facts_dao.InterestingFactsDAO()
