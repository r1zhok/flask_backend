from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.review_controller import ReviewController
from my_project.auth.domain.orders.review import Review

review_bp = Blueprint('reviews', __name__, url_prefix='/reviews')
review = ReviewController()


@review_bp.get('')
def get_all_descriptions() -> Response:
    return make_response(jsonify(review.find_all()), HTTPStatus.OK)


@review_bp.post('')
def create_description() -> Response:
    content = request.get_json()
    return make_response(jsonify(review.create(Review.create_from_dto(content))), HTTPStatus.CREATED)


@review_bp.get('/<int:review_id>')
def get_description(review_id: int) -> Response:
    return make_response(jsonify(review.find_by_id(review_id)), HTTPStatus.OK)


@review_bp.put('/<int:review_id>')
def update_description(review_id: int) -> Response:
    review.update(review_id, Review.create_from_dto(request.get_json()))
    return make_response("Review updated", HTTPStatus.OK)


@review_bp.patch('/<int:review_id>')
def patch_description(review_id: int) -> Response:
    review.patch(review_id, request.get_json())
    return make_response("Review updated", HTTPStatus.OK)


@review_bp.delete('/<int:review_id>')
def delete_description(review_id: int) -> Response:
    review.delete(review_id)
    return make_response("Review deleted", HTTPStatus.OK)
