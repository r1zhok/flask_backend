"""
2023
oleksii.strizhyk.ir.2022@lpnu.ua
© Oleksii Strizhyk
"""

from __future__ import annotations

from typing import Dict, Any

from my_project import db


class FilmHasRating(db.Model):
    """
    Model declaration for the junction table 'film_has_rating'.
    """
    __tablename__ = "film_has_rating"

    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), primary_key=True, nullable=False)
    rating_id = db.Column(db.Integer, db.ForeignKey('rating.id'), primary_key=True, nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "film_id": self.film_id,
            "rating_id": self.rating_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> FilmHasRating:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = FilmHasRating(
            film_id=dto_dict.get("film_id"),
            rating_id=dto_dict.get("rating_id")
        )
        return obj

    def __repr__(self) -> str:
        return f"FilmHasRating({self.film_id}, {self.rating_id})"
