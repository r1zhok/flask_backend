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
