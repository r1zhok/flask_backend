from typing import Dict, Any

from my_project import db


class AdditionalTable(db.Model):
    """
    Model declaration for Data Mapper for the additional table.
    """
    __tablename__ = "additional_table"

    additional_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    additional_data = db.Column(db.String(255), nullable=False)
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'), nullable=False)
    actor = db.relationship('Actor', backref=db.backref('additional_data', lazy=True))

    def __repr__(self) -> str:
        return f"AdditionalTable({self.additional_id}, '{self.additional_data}', {self.actor_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.additional_id,
            "additional_data": self.additional_data,
            "actor_id": self.actor_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]):
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = AdditionalTable(
            additional_data=dto_dict.get("additional_data"),
            actor_id=dto_dict.get("actor_id")
        )
        return obj
