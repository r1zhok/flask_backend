from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.roles_controller import RolesController
from my_project.auth.domain.orders.roles import Role

role_bp = Blueprint('roles', __name__, url_prefix='/roles')
role = RolesController()


@role_bp.get('')
def get_all_descriptions() -> Response:
    return make_response(jsonify(role.find_all()), HTTPStatus.OK)


@role_bp.post('')
def create_description() -> Response:
    content = request.get_json()
    return make_response(jsonify(role.create(Role.create_from_dto(content))), HTTPStatus.CREATED)


@role_bp.get('/<int:roles_id>')
def get_description(roles_id: int) -> Response:
    return make_response(jsonify(role.find_by_id(roles_id)), HTTPStatus.OK)


@role_bp.put('/<int:roles_id>')
def update_description(roles_id: int) -> Response:
    role.update(roles_id, Role.create_from_dto(request.get_json()))
    return make_response("Role updated", HTTPStatus.OK)


@role_bp.patch('/<int:roles_id>')
def patch_description(roles_id: int) -> Response:
    role.patch(roles_id, request.get_json())
    return make_response("Role updated", HTTPStatus.OK)


@role_bp.delete('/<int:roles_id>')
def delete_description(roles_id: int) -> Response:
    role.delete(roles_id)
    return make_response("Role deleted", HTTPStatus.OK)
