"""
2023
oleksii.strizhyk.ir.2022@lpnu.ua
© Oleksii Strizhyk
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Rating(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "rating"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mark = db.Column(db.String(45), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    films = db.relationship('Film', secondary='film_has_rating', back_populates='rating')
    person = db.relationship('Person', backref=db.backref('ratings', lazy=True))

    def __repr__(self) -> str:
        return f"Rating({self.id}, '{self.mark}', {self.person_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "mark": self.mark,
            "person_id": self.person_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Rating:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Rating(
            mark=dto_dict.get("mark"),
            person_id=dto_dict.get("person_id")
        )
        return obj
