"""
2023
oleksii.strizhyk.ir.2022@lpnu.ua
© Oleksii Strizhyk
"""
from my_project.auth.dao.orders import actor_dao
from my_project.auth.service.general_service import GeneralService


class ActorService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = actor_dao.ActorDAO()

    def insert_actor(self, p_name: str, p_surname: str, p_age: int, p_film_id: int):
        return self._dao.insert_actor(p_name, p_surname, p_age, p_film_id)

    def insert_noname_actors(self):
        return self._dao.insert_noname_actors()

    def get_statistic(self):
        return self._dao.get_statistic()
