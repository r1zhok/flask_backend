from typing import Dict, Any


class Test:

    def __init__(self, name, mark, person_id):
        self.name = name
        self.mark = mark
        self.person_id = person_id

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "mark": self.mark,
            "person_id": self.person_id,
    }