from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.person_controller import PersonController
from my_project.auth.controller.orders.rating_controller import RatingController
from my_project.auth.controller.orders.review_controller import ReviewController
from my_project.auth.domain.orders.person import Person

person_bp = Blueprint('persons', __name__, url_prefix='/persons')
person = PersonController()
rating = RatingController()
review = ReviewController()


@person_bp.get('')
def get_all_person() -> Response:
    return make_response(jsonify(person.find_all()), HTTPStatus.OK)


@person_bp.post('')
def create_person() -> Response:
    content = request.get_json()
    return make_response(jsonify(person.create(Person.create_from_dto(content))), HTTPStatus.CREATED)


@person_bp.get('/<int:person_id>')
def get_person(person_id: int) -> Response:
    return make_response(jsonify(person.find_by_id(person_id)), HTTPStatus.OK)


@person_bp.put('/<int:person_id>')
def update_person(person_id: int) -> Response:
    person.update(person_id, Person.create_from_dto(request.get_json()))
    return make_response("Person updated", HTTPStatus.OK)


@person_bp.patch('/<int:person_id>')
def patch_person(person_id: int) -> Response:
    person.patch(person_id, request.get_json())
    return make_response("Person updated", HTTPStatus.OK)


@person_bp.delete('/<int:person_id>')
def delete_person(person_id: int) -> Response:
    person.delete(person_id)
    return make_response("Person deleted", HTTPStatus.OK)


@person_bp.get('/<int:person_id>/rating')
def get_all_person_role(person_id: int) -> Response:
    return make_response(jsonify(rating.get_person_rating(person_id)), HTTPStatus.OK)


@person_bp.get('/<int:person_id>/review')
def get_all_person_reviews(person_id: int) -> Response:
    return make_response(jsonify(review.get_person_reviews(person_id)), HTTPStatus.OK)
