"""
2023
oleksii.strizhyk.ir.2022@lpnu.ua
© Oleksii Strizhyk
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Review(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    review = db.Column(db.String(225), nullable=False)
    creation_date = db.Column(db.Date, nullable=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    films = db.relationship('Film', secondary='review_has_film', back_populates='review')

    person = db.relationship('Person', backref=db.backref('reviews', lazy=True))

    def __repr__(self) -> str:
        return f"Review({self.id}, '{self.review}', {self.creation_date}, {self.person_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "review": self.review,
            "creation_date": str(self.creation_date) if self.creation_date else None,
            "person_id": self.person_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Review:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Review(
            review=dto_dict.get("review"),
            creation_date=dto_dict.get("creation_date"),
            person_id=dto_dict.get("person_id")
        )
        return obj
