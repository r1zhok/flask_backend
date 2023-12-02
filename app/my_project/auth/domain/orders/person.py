"""
2023
oleksii.strizhyk.ir.2022@lpnu.ua
© Oleksii Strizhyk
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Person(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False, index=True)
    birthdate = db.Column(db.Date, nullable=True)

    def __repr__(self) -> str:
        return f"Person({self.id}, '{self.name}', '{self.surname}', {self.birthdate})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "birthdate": str(self.birthdate) if self.birthdate else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Person:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Person(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            birthdate=dto_dict.get("birthdate")
        )
        return obj
