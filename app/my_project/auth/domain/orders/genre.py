"""
2023
oleksii.strizhyk.ir.2022@lpnu.ua
© Oleksii Strizhyk
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Genre(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "genre"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(45), nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=False)

    film = db.relationship('Film', backref=db.backref('genres', lazy=True))

    def __repr__(self) -> str:
        return f"Genre({self.id}, '{self.type}', {self.film_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "type": self.type,
            "film_id": self.film_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Genre:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Genre(
            type=dto_dict.get("type"),
            film_id=dto_dict.get("film_id")
        )
        return obj
