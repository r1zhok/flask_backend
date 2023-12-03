from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.roles import Role


class RolesDAO(GeneralDAO):
    """
    Realisation of Roles data access layer.
    """
    _domain_type = Role

    def find_by_role(self, role: str) -> Role:
        """
        Gets Roles object from the database table by field role.
        :param role: role value
        :return: Roles object
        """
        return self._session.query(Role).filter(Role.role == role).first()

    def find_by_actor_id(self, actor_id: int) -> List[Role]:
        """
        Gets Roles objects from the database table by field actor_id.
        :param actor_id: actor_id value
        :return: List of Roles objects
        """
        return self._session.query(Role).filter(Role.actor_id == actor_id).all()

    def find_all(self):
        return Role.query.all()
