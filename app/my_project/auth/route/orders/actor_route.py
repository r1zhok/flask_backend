from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

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


@actor_bp.get('/<int:actor_id>')
def get_actor(actor_id: int) -> Response:
    return make_response(jsonify(actor.find_by_id(actor_id)), HTTPStatus.OK)


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
