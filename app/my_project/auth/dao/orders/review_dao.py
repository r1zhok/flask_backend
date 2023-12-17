from datetime import date
from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.review import Review


class ReviewDAO(GeneralDAO):
    """
    Realisation of Review data access layer.
    """
    _domain_type = Review

    def find_by_creation_date(self, creation_date: date) -> List[Review]:
        """
        Gets Review objects from the database table by field creation_date.
        :param creation_date: creation_date value
        :return: List of Review objects
        """
        return self._session.query(Review).filter(Review.creation_date == creation_date).all()

    def find_all(self):
        return Review.query.all()

    def get_person_rating(self, person_id):
        return self._session.query(Review).filter(Review.person_id == person_id).order_by(Review.person_id).all()
