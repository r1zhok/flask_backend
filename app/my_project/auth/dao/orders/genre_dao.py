from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.genre import Genre


class GenreDAO(GeneralDAO):
    """
    Realisation of Genre data access layer.
    """
    _domain_type = Genre

    def find_by_type(self, genre_type: str) -> Genre:
        """
        Gets Genre object from the database table by field type.
        :param genre_type: genre_type value
        :return: Genre object
        """
        return self._session.query(Genre).filter(Genre.type == genre_type).first()

    def find_all(self):
        return Genre.query.all()
