from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.review_has_film_controller import ReviewHasFilmController
from my_project.auth.domain import Film
from my_project.auth.domain.orders.films_and_review import FilmsAndReview
from my_project.auth.domain.orders.review_has_film import ReviewHasFilm

review_has_film_bp = Blueprint('review_has_film', __name__, url_prefix='/review_has_film')
review_has_film = ReviewHasFilmController()


@review_has_film_bp.get('')
def get_all_descriptions() -> Response:
    return make_response(jsonify(review_has_film.find_all()), HTTPStatus.OK)


@review_has_film_bp.get('all_data')
def get_all_data() -> Response:
    films = Film.query.all()
    massive = []
    for film in films:
        for review in film.review:
            massive.append(FilmsAndReview(film.name, review.review, review.creation_date).to_dict())

    return make_response(jsonify(massive), HTTPStatus.OK)


@review_has_film_bp.post('')
def create_description() -> Response:
    content = request.get_json()
    return make_response(jsonify(review_has_film.create(ReviewHasFilm.create_from_dto(content))), HTTPStatus.CREATED)


@review_has_film_bp.get('/<int:review_has_film_id>')
def get_description(review_has_film_id: int) -> Response:
    return make_response(jsonify(review_has_film.find_by_id(review_has_film_id)), HTTPStatus.OK)


@review_has_film_bp.put('/<int:review_has_film_id>')
def update_description(review_has_film_id: int) -> Response:
    review_has_film.update(review_has_film_id, ReviewHasFilm.create_from_dto(request.get_json()))
    return make_response("ReviewHasFilm updated", HTTPStatus.OK)


@review_has_film_bp.patch('/<int:review_has_film_id>')
def patch_description(review_has_film_id: int) -> Response:
    review_has_film.patch(review_has_film_id, request.get_json())
    return make_response("ReviewHasFilm updated", HTTPStatus.OK)


@review_has_film_bp.delete('/<int:review_has_film_id>')
def delete_description(review_has_film_id: int) -> Response:
    review_has_film.delete(review_has_film_id)
    return make_response("ReviewHasFilm deleted", HTTPStatus.OK)
