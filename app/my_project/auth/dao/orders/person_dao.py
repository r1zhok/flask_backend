from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.person import Person


class PersonDAO(GeneralDAO):
    """
    Realisation of Person data access layer.
    """
    _domain_type = Person

    def find_by_name_and_surname(self, name: str, surname: str) -> Person:
        """
        Gets Person object from the database table by fields name and surname.
        :param name: name value
        :param surname: surname value
        :return: Person object
        """
        return (
            self._session.query(Person)
            .filter(Person.name == name, Person.surname == surname)
            .first()
        )

    def find_all(self):
        return Person.query.all()
