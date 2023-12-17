from my_project.auth.service.orders import actor_service
from my_project.auth.controller.general_controller import GeneralController


class ActorController(GeneralController):
    """
    Realisation of Actor controller.
    """
    _service = actor_service.ActorService()

    def insert_actor(self, p_name: str, p_surname: str, p_age: int, p_film_id: int):
        return self._service.insert_actor(p_name, p_surname, p_age, p_film_id)

    def insert_noname_actors(self):
        return self._service.insert_noname_actors()

    def get_statistic(self):
        return self._service.get_statistic()

    def create_dynamic_tables(self):
        self._service.create_dynamic_tables()
