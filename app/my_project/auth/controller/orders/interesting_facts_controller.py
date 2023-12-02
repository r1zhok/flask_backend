from my_project.auth.service.orders import interesting_facts_service
from my_project.auth.controller.general_controller import GeneralController


class InterestingFactsController(GeneralController):
    """
    Realisation of InterestingFacts controller.
    """
    _service = interesting_facts_service.InterestingFactsService()
