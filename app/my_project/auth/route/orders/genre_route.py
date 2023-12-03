from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.genre_controller import GenreController
from my_project.auth.domain.orders.genre import Genre

genre_bp = Blueprint('genres', __name__, url_prefix='/genres')
genre = GenreController()


@genre_bp.get('')
def get_all_descriptions() -> Response:
    return make_response(jsonify(genre.find_all()), HTTPStatus.OK)


@genre_bp.post('')
def create_description() -> Response:
    content = request.get_json()
    return make_response(jsonify(genre.create(Genre.create_from_dto(content))), HTTPStatus.CREATED)


@genre_bp.get('/<int:genre_id>')
def get_description(genre_id: int) -> Response:
    return make_response(jsonify(genre.find_by_id(genre_id)), HTTPStatus.OK)


@genre_bp.put('/<int:genre_id>')
def update_description(genre_id: int) -> Response:
    genre.update(genre_id, Genre.create_from_dto(request.get_json()))
    return make_response("Genre updated", HTTPStatus.OK)


@genre_bp.patch('/<int:genre_id>')
def patch_description(genre_id: int) -> Response:
    genre.patch(genre_id, request.get_json())
    return make_response("Genre updated", HTTPStatus.OK)


@genre_bp.delete('/<int:genre_id>')
def delete_description(genre_id: int) -> Response:
    genre.delete(genre_id)
    return make_response("Genre deleted", HTTPStatus.OK)
