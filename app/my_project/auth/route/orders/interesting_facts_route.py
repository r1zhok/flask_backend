from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.interesting_facts_controller import InterestingFactsController
from my_project.auth.domain.orders.interesting_facts import InterestingFact

interesting_facts_bp = Blueprint('interesting_facts', __name__, url_prefix='/interesting_facts')
interesting_facts = InterestingFactsController()


@interesting_facts_bp.get('')
def get_all_descriptions() -> Response:
    return make_response(jsonify(interesting_facts.find_all()), HTTPStatus.OK)


@interesting_facts_bp.post('')
def create_description() -> Response:
    content = request.get_json()
    return make_response(jsonify(interesting_facts.create(InterestingFact.create_from_dto(content))),
                         HTTPStatus.CREATED)


@interesting_facts_bp.get('/<int:interesting_fact>')
def get_description(interesting_fact: int) -> Response:
    return make_response(jsonify(interesting_facts.find_by_id(interesting_fact)), HTTPStatus.OK)


@interesting_facts_bp.put('/<int:interesting_fact>')
def update_description(interesting_fact: int) -> Response:
    interesting_facts.update(interesting_fact, InterestingFact.create_from_dto(request.get_json()))
    return make_response("InterestingFact updated", HTTPStatus.OK)


@interesting_facts_bp.patch('/<int:interesting_fact>')
def patch_description(interesting_fact: int) -> Response:
    interesting_facts.patch(interesting_fact, request.get_json())
    return make_response("InterestingFact updated", HTTPStatus.OK)


@interesting_facts_bp.delete('/<int:interesting_fact>')
def delete_description(interesting_fact: int) -> Response:
    interesting_facts.delete(interesting_fact)
    return make_response("InterestingFact deleted", HTTPStatus.OK)
