from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.film_controller import FilmController
from my_project.auth.domain.orders.film import Film

film_bp = Blueprint('films', __name__, url_prefix='/films')
film = FilmController()


@film_bp.get('')
def get_all_films() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(film.find_all()), HTTPStatus.OK)


@film_bp.post('')
def create_films() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    return make_response(jsonify(film.create(Film.create_from_dto(content))), HTTPStatus.CREATED)


@film_bp.get('/<int:film_id>')
def get_film(film_id: int) -> Response:
    """
    Gets film by ID.
    :return: Response object
    """
    return make_response(jsonify(film.find_by_id(film_id)), HTTPStatus.OK)


@film_bp.put('/<int:film_id>')
def update_film(film_id: int) -> Response:
    """
    Updates film by ID.
    :return: Response object
    """
    film.update(film_id, Film.create_from_dto(request.get_json()))
    return make_response("Client updated", HTTPStatus.OK)


@film_bp.patch('/<int:film_id>')
def patch_film(film_id: int) -> Response:
    """
    Patches film by ID.
    :return: Response object
    """
    film.patch(film_id, request.get_json())
    return make_response("Client updated", HTTPStatus.OK)


@film_bp.delete('/<int:film_id>')
def delete_film(film_id: int) -> Response:
    """
    Deletes film by ID.
    :return: Response object
    """
    film.delete(film_id)
    return make_response("Client deleted", HTTPStatus.OK)
