from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.description import Description


class DescriptionDAO(GeneralDAO):
    """
    Realisation of Description data access layer.
    """
    _domain_type = Description

    def find_by_film_id(self, film_id: int) -> Description:
        """
        Gets Description object from the database table by field film_id.
        :param film_id: film_id value
        :return: Description object
        """
        return self._session.query(Description).filter(Description.film_id == film_id).first()

    def find_all(self):
        return Description.query.all()
