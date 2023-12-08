from typing import Dict, Any


class FilmsAndReview:

    def __init__(self, name, review, creation_date):
        self.name = name
        self.review = review
        self.creation_date = creation_date

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "review": self.review,
            "creation_date": self.creation_date,
    }