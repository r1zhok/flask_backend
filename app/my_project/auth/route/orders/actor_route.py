from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response
from sqlalchemy import RowMapping

from my_project.auth.controller.orders import actor_controller
from my_project.auth.domain.orders.actor import Actor
from my_project.auth.dao.orders.roles_dao import RolesDAO

actor_bp = Blueprint('actors', __name__, url_prefix='/actors')
actor = actor_controller.ActorController()
roles_dao = RolesDAO()


@actor_bp.get('')
def get_all_actors() -> Response:
    return make_response(jsonify(actor.find_all()), HTTPStatus.OK)


@actor_bp.post('')
def create_actor() -> Response:
    content = request.get_json()
    return make_response(jsonify(actor.create(Actor.create_from_dto(content))), HTTPStatus.CREATED)


@actor_bp.post('/insert')
def insert_actor():
    data = request.get_json()
    p_name = data.get('name')
    p_surname = data.get('surname')
    p_age = data.get('age')
    p_film_id = data.get('film_id')

    result = actor.insert_actor(p_name, p_surname, p_age, p_film_id)

    if result is not None:
        if isinstance(result, dict):
            result = [result]
        elif isinstance(result, RowMapping):
            result = [dict(result)]
        elif isinstance(result, list) and all(isinstance(row, RowMapping) for row in result):
            result = [dict(row) for row in result]

        formatted_result = [{"id": row["id"], "name": row["name"], "surname": row["surname"], "age": row["age"],
                             "film_id": row["film_id"]} for row in result]

        return make_response(jsonify(formatted_result), HTTPStatus.CREATED)
    else:
        return make_response(jsonify({"error": "Failed to insert actor"}), HTTPStatus.INTERNAL_SERVER_ERROR)


@actor_bp.post('/no_name')
def insert_no_name_actor():
    result = actor.insert_noname_actors()
    if result is not None:
        if isinstance(result, dict):
            result = [result]
        elif isinstance(result, RowMapping):
            result = [dict(result)]
        elif isinstance(result, list) and all(isinstance(row, RowMapping) for row in result):
            result = [dict(row) for row in result]

        return make_response(jsonify(result), HTTPStatus.CREATED)
    else:
        return make_response(jsonify({"error": "Failed to insert actor"}), HTTPStatus.INTERNAL_SERVER_ERROR)


@actor_bp.get('/<int:actor_id>')
def get_actor(actor_id: int) -> Response:
    return make_response(jsonify(actor.find_by_id(actor_id)), HTTPStatus.OK)


@actor_bp.get('/get_statistic')
def get_statistic() -> Response:
    result = actor.get_statistic()
    if result is not None:
        if isinstance(result, dict):
            result = [result]
        elif isinstance(result, RowMapping):
            result = [dict(result)]
        elif isinstance(result, list) and all(isinstance(row, RowMapping) for row in result):
            result = [dict(row) for row in result]

        return make_response(jsonify(result), HTTPStatus.CREATED)
    else:
        return make_response(jsonify({"error": "Failed to insert actor"}), HTTPStatus.INTERNAL_SERVER_ERROR)


@actor_bp.put('/<int:actor_id>')
def update_actor(actor_id: int) -> Response:
    content = request.get_json()
    actor.update(actor_id, Actor.create_from_dto(content))
    return make_response("Actor updated", HTTPStatus.OK)


@actor_bp.patch('/<int:actor_id>')
def patch_actor(actor_id: int) -> Response:
    content = request.get_json()
    actor.patch(actor_id, content)
    return make_response("Actor updated", HTTPStatus.OK)


@actor_bp.delete('/<int:actor_id>')
def delete_actor(actor_id: int) -> Response:
    actor.delete(actor_id)
    return make_response("Actor deleted", HTTPStatus.OK)


@actor_bp.get('/<int:actor_id>/roles')
def get_actor_roles(actor_id: int) -> Response:
    actor_roles = roles_dao.find_by_actor_id(actor_id)
    roles_data = [role.to_dict() for role in actor_roles]
    return make_response(jsonify(roles_data), HTTPStatus.OK)
