from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.film import Film


class FilmDAO(GeneralDAO):
    """
    Realisation of Film data access layer.
    """
    _domain_type = Film

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Film objects from the database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Film).filter(Film.name == name).order_by(Film.name).all()

    def find_by_id(self, film_id: int) -> Film:
        """
        Gets Film object from the database table by ID.
        :param film_id: ID of the film
        :return: Film object
        """
        return self._session.query(Film).get(film_id)

    def find_all(self):
        return Film.query.all()
