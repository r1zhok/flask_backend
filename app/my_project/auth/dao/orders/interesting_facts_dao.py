from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.interesting_facts import InterestingFact


class InterestingFactsDAO(GeneralDAO):
    """
    Realisation of InterestingFacts data access layer.
    """
    _domain_type = InterestingFact

    def find_by_fact(self, fact: str) -> InterestingFact:
        """
        Gets InterestingFacts object from the database table by field fact.
        :param fact: fact value
        :return: InterestingFacts object
        """
        return self._session.query(InterestingFact).filter(InterestingFact.fact == fact).first()

    def find_all(self):
        return InterestingFact.query.all()
