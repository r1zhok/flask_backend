from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.additional_table import AdditionalTable


class AddingTableDAO(GeneralDAO):
    _domain_type = AdditionalTable

    def find_all(self):
        return AdditionalTable.query.all()
