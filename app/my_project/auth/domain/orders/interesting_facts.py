"""
2023
oleksii.strizhyk.ir.2022@lpnu.ua
© Oleksii Strizhyk
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class InterestingFact(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "interesting_facts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fact = db.Column(db.String(45), nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=False)

    film = db.relationship('Film', backref=db.backref('interesting_facts', lazy=True))

    def __repr__(self) -> str:
        return f"InterestingFact({self.id}, '{self.fact}', {self.film_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "fact": self.fact,
            "film_id": self.film_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> InterestingFact:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = InterestingFact(
            fact=dto_dict.get("fact"),
            film_id=dto_dict.get("film_id")
        )
        return obj
