from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.rating_controller import RatingController
from my_project.auth.domain.orders.rating import Rating

rating_bp = Blueprint('ratings', __name__, url_prefix='/ratings')
rating = RatingController()


@rating_bp.get('')
def get_all_descriptions() -> Response:
    return make_response(jsonify(rating.find_all()), HTTPStatus.OK)


@rating_bp.post('')
def create_description() -> Response:
    content = request.get_json()
    return make_response(jsonify(rating.create(Rating.create_from_dto(content))), HTTPStatus.CREATED)


@rating_bp.get('/<int:rating_id>')
def get_description(rating_id: int) -> Response:
    return make_response(jsonify(rating.find_by_id(rating_id)), HTTPStatus.OK)


@rating_bp.put('/<int:rating_id>')
def update_description(rating_id: int) -> Response:
    rating.update(rating_id, Rating.create_from_dto(request.get_json()))
    return make_response("Rating updated", HTTPStatus.OK)


@rating_bp.patch('/<int:rating_id>')
def patch_description(rating_id: int) -> Response:
    rating.patch(rating_id, request.get_json())
    return make_response("Rating updated", HTTPStatus.OK)


@rating_bp.delete('/<int:rating_id>')
def delete_description(rating_id: int) -> Response:
    rating.delete(rating_id)
    return make_response("Rating deleted", HTTPStatus.OK)
