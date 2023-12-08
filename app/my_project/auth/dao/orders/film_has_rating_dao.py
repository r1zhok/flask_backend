from sqlalchemy import text

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.film_has_rating import FilmHasRating


class FilmHasRatingDAO(GeneralDAO):
    """
    Realisation of FilmHasRating data access layer.
    """
    _domain_type = FilmHasRating

    def find_by_film_id_and_rating_id(self, film_id: int, rating_id: int) -> FilmHasRating:
        """
        Gets FilmHasRating object from the database table by fields film_id and rating_id.
        :param film_id: film_id value
        :param rating_id: rating_id value
        :return: FilmHasRating object
        """
        return (
            self._session.query(FilmHasRating)
            .filter(FilmHasRating.film_id == film_id, FilmHasRating.rating_id == rating_id)
            .first()
        )

    def find_all(self):
        return FilmHasRating.query.all()

    def insert_data_procedure(self, p_name: str, mark: int):
        query = text("CALL insert_data_procedure(:p_name, :mark)")
        self._session.execute(query, {"p_name": p_name, "mark": mark})