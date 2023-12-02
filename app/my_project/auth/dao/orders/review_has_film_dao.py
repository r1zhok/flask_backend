from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.review_has_film import ReviewHasFilm


class ReviewHasFilmDAO(GeneralDAO):
    """
    Realisation of ReviewHasFilm data access layer.
    """
    _domain_type = ReviewHasFilm

    def find_by_review_id(self, review_id: int) -> ReviewHasFilm:
        """
        Gets ReviewHasFilm object from the database table by field review_id.
        :param review_id: review_id value
        :return: ReviewHasFilm object
        """
        return self._session.query(ReviewHasFilm).filter(ReviewHasFilm.review_id == review_id).first()

    def find_by_film_id(self, film_id: int) -> ReviewHasFilm:
        """
        Gets ReviewHasFilm object from the database table by field film_id.
        :param film_id: film_id value
        :return: ReviewHasFilm object
        """
        return self._session.query(ReviewHasFilm).filter(ReviewHasFilm.film_id == film_id).first()

    def find_all(self):
        return ReviewHasFilm.query.all()
