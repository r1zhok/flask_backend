from typing import List

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.actor import Actor


class ActorDAO(GeneralDAO):
    """
    Realisation of Actor data access layer.
    """
    _domain_type = Actor

    def find_by_name(self, name: str) -> List[Actor]:
        """
        Gets Actor objects from the database table by field name.
        :param name: name value
        :return: list of Actor objects
        """
        return self._session.query(Actor).filter(Actor.name == name).order_by(Actor.name).all()

    def find_by_surname(self, surname: str) -> List[Actor]:
        """
        Gets Actor objects from the database table by field surname.
        :param surname: surname value
        :return: list of Actor objects
        """
        return self._session.query(Actor).filter(Actor.surname == surname).order_by(Actor.surname).all()

    def find_by_age(self, age: int) -> List[Actor]:
        """
        Gets Actor objects from the database table by field age.
        :param age: age value
        :return: list of Actor objects
        """
        return self._session.query(Actor).filter(Actor.age == age).order_by(Actor.age).all()

    def find_by_film_id(self, film_id: int) -> List[Actor]:
        """
        Gets Actor objects from the database table by field film_id.
        :param film_id: film_id value
        :return: list of Actor objects
        """
        return self._session.query(Actor).filter(Actor.film_id == film_id).order_by(Actor.film_id).all()

    def find_all(self):
        return Actor.query.all()

    def insert_actor(self, p_name: str, p_surname: str, p_age: int, p_film_id: int) -> None:
        """
        Inserts a new actor into the 'actor' table using a stored procedure.
        :param p_name: Name of the actor
        :param p_surname: Surname of the actor
        :param p_age: Age of the actor
        :param p_film_id: Film ID related to the actor
        """
        params = {"p_name": p_name, "p_surname": p_surname, "p_age": p_age, "p_film_id": p_film_id}

        return self._session.execute(sqlalchemy.text(f"CALL insert_actor(:p_name, :p_surname, :p_age, :p_film_id)"),
                                     params).mappings().all()

    def insert_noname_actors(self):
        self._session.begin()
        result = self._session.execute(sqlalchemy.text(f"CALL insert_noname_actors()")).mappings().all()
        self._session.commit()
        return result

    def get_statistic(self):
        return self._session.execute(sqlalchemy.text(f"CALL get_actor_statistics()")).mappings().all()