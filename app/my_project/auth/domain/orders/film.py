"""
2023
oleksii.strizhyk.ir.2022@lpnu.ua
© Oleksii Strizhyk
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Film(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "film"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), index=True)
    rating = db.relationship('Rating', secondary='film_has_rating', back_populates='films')
    review = db.relationship('Review', secondary='review_has_film', back_populates='films')

    def __repr__(self) -> str:
        return f"Film({self.id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Film:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Film(
            name=dto_dict.get("name")
        )
        return obj

