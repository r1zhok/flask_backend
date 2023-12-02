"""
2023
oleksii.strizhyk.ir.2022@lpnu.ua
© Oleksii Strizhyk
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Actor(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "actor"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), index=True)
    surname = db.Column(db.String(45))
    age = db.Column(db.Integer, nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=False)
    film = db.relationship('Film', backref=db.backref('actors', lazy=True))

    def __repr__(self) -> str:
        return f"Actor({self.id}, '{self.name}', '{self.surname}', {self.age}, {self.film_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "film_id": self.film_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Actor:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Actor(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            age=dto_dict.get("age"),
            film_id=dto_dict.get("film_id")
        )
        return obj
