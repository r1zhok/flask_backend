from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.film_has_rating_controller import FilmHasRatingController
from my_project.auth.domain.orders.film import Film
from my_project.auth.domain.orders.film_has_rating import FilmHasRating
from my_project.auth.domain.orders.films_and_rating import FilmsAndRating

film_has_rating_bp = Blueprint('film_has_ratings', __name__, url_prefix='/film_has_ratings')
film_has_rating = FilmHasRatingController()


@film_has_rating_bp.get('')
def get_all_descriptions() -> Response:
    return make_response(jsonify(film_has_rating.find_all()), HTTPStatus.OK)


@film_has_rating_bp.get('/all_data')
def get_all_data() -> Response():
    films = Film.query.all()
    massive = []
    for film in films:
        for rating in film.rating:
            massive.append(FilmsAndRating(film.name, rating.mark, rating.person_id).to_dict())

    return make_response(jsonify(massive), HTTPStatus.OK)


@film_has_rating_bp.post('')
def create_description() -> Response:
    content = request.get_json()
    film_has_rating.insert_data_procedure(content.get("name"), content.get("mark"), content.get("person_id"))
    return make_response("FilmHasRating created and father tables created", HTTPStatus.OK)


@film_has_rating_bp.get('/<int:film_has_rating_id>')
def get_description(film_has_rating_id: int) -> Response:
    return make_response(jsonify(film_has_rating.find_by_id(film_has_rating_id)), HTTPStatus.OK)


@film_has_rating_bp.put('/<int:film_has_rating_id>')
def update_description(film_has_rating_id: int) -> Response:
    content = request.get_json()
    film_has_rating.update(film_has_rating_id, FilmHasRating.create_from_dto(content))
    return make_response("FilmHasRating updated", HTTPStatus.OK)


@film_has_rating_bp.patch('/<int:film_has_rating_id>')
def patch_description(film_has_rating_id: int) -> Response:
    content = request.get_json()
    film_has_rating.patch(film_has_rating_id, content)
    return make_response("FilmHasRating updated", HTTPStatus.OK)


@film_has_rating_bp.delete('/<int:film_has_rating_id>')
def delete_description(film_has_rating_id: int) -> Response:
    film_has_rating.delete(film_has_rating_id)
    return make_response("FilmHasRating deleted", HTTPStatus.OK)
