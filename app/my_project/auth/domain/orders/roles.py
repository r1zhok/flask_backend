from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Role(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(45), nullable=False)
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'), nullable=False)

    actor = db.relationship('Actor', backref=db.backref('roles', lazy=True))

    def __repr__(self) -> str:
        return f"Role({self.id}, '{self.role}', {self.actor_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "role": self.role,
            "actor_id": self.actor_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Role:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Role(
            role=dto_dict.get("role"),
            actor_id=dto_dict.get("actor_id")
        )
        return obj

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "role": self.role,
            "actor_id": self.actor_id,
        }
