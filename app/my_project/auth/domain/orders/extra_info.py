"""
2023
oleksii.strizhyk.ir.2022@lpnu.ua
© Oleksii Strizhyk
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class ExtraInfo(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "extra_info"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    release_year = db.Column(db.Date, nullable=True)
    duration = db.Column(db.Integer, nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=False)

    film = db.relationship('Film', backref=db.backref('extra_info', lazy=True))

    def __repr__(self) -> str:
        return f"ExtraInfo({self.id}, {self.release_year}, {self.duration}, {self.film_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "release_year": str(self.release_year) if self.release_year else None,
            "duration": self.duration,
            "film_id": self.film_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ExtraInfo:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ExtraInfo(
            release_year=dto_dict.get("release_year"),
            duration=dto_dict.get("duration"),
            film_id=dto_dict.get("film_id")
        )
        return obj
