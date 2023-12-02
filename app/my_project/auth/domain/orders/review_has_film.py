"""
2023
oleksii.strizhyk.ir.2022@lpnu.ua
© Oleksii Strizhyk
"""

from __future__ import annotations
from my_project import db


class ReviewHasFilm(db.Model):
    """
    Model declaration for the junction table 'review_has_film'.
    """
    __tablename__ = "review_has_film"

    review_id = db.Column(db.Integer, db.ForeignKey('review.id'), primary_key=True, nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), primary_key=True, nullable=False)

    def __repr__(self) -> str:
        return f"ReviewHasFilm({self.review_id}, {self.film_id})"
