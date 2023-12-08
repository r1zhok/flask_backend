from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.rating import Rating


class RatingDAO(GeneralDAO):
    """
    Realisation of Rating data access layer.
    """
    _domain_type = Rating

    def find_by_mark(self, mark: str) -> Rating:
        """
        Gets Rating object from the database table by field mark.
        :param mark: mark value
        :return: Rating object
        """
        return self._session.query(Rating).filter(Rating.mark == mark).first()

    def find_all(self):
        return Rating.query.all()

    def get_person_rating(self, person_id: int) -> List[Rating]:
        """
        Gets Actor objects from the database table by field film_id.
        :param person_id: film_id value
        :return: list of Actor objects
        """
        return self._session.query(Rating).filter(Rating.person_id == person_id).order_by(Rating.person_id).all()
