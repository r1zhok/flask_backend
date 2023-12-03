from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.person_controller import PersonController
from my_project.auth.domain.orders.person import Person

person_bp = Blueprint('persons', __name__, url_prefix='/persons')
person = PersonController()


@person_bp.get('')
def get_all_descriptions() -> Response:
    return make_response(jsonify(person.find_all()), HTTPStatus.OK)


@person_bp.post('')
def create_description() -> Response:
    content = request.get_json()
    return make_response(jsonify(person.create(Person.create_from_dto(content))), HTTPStatus.CREATED)


@person_bp.get('/<int:person_id>')
def get_description(person_id: int) -> Response:
    return make_response(jsonify(person.find_by_id(person_id)), HTTPStatus.OK)


@person_bp.put('/<int:person_id>')
def update_description(person_id: int) -> Response:
    person.update(person_id, Person.create_from_dto(request.get_json()))
    return make_response("Person updated", HTTPStatus.OK)


@person_bp.patch('/<int:person_id>')
def patch_description(person_id: int) -> Response:
    person.patch(person_id, request.get_json())
    return make_response("Person updated", HTTPStatus.OK)


@person_bp.delete('/<int:person_id>')
def delete_description(person_id: int) -> Response:
    person.delete(person_id)
    return make_response("Person deleted", HTTPStatus.OK)
