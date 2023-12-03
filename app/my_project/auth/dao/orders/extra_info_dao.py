from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.extra_info import ExtraInfo


class ExtraInfoDAO(GeneralDAO):
    """
    Realisation of ExtraInfo data access layer.
    """
    _domain_type = ExtraInfo

    def find_by_film_id(self, film_id: int) -> ExtraInfo:
        """
        Gets ExtraInfo object from the database table by field film_id.
        :param film_id: film_id value
        :return: ExtraInfo object
        """
        return self._session.query(ExtraInfo).filter(ExtraInfo.film_id == film_id).first()

    def find_by_release_year(self, release_year: str) -> ExtraInfo:
        """
        Gets ExtraInfo object from the database table by field release_year.
        :param release_year: release_year value
        :return: ExtraInfo object
        """
        return self._session.query(ExtraInfo).filter(ExtraInfo.release_year == release_year).first()

    def find_by_duration(self, duration: int) -> ExtraInfo:
        """
        Gets ExtraInfo object from the database table by field duration.
        :param duration: duration value
        :return: ExtraInfo object
        """
        return self._session.query(ExtraInfo).filter(ExtraInfo.duration == duration).first()

    def find_all(self):
        return ExtraInfo.query.all()
