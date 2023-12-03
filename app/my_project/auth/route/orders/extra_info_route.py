from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders import extra_info_controller
from my_project.auth.domain.orders.extra_info import ExtraInfo

extra_info_bp = Blueprint('extra_info', __name__, url_prefix='/extra_info')
extra_info = extra_info_controller.ExtraInfoController()


@extra_info_bp.get('')
def get_all_descriptions() -> Response:
    return make_response(jsonify(extra_info.find_all()), HTTPStatus.OK)


@extra_info_bp.post('')
def create_description() -> Response:
    content = request.get_json()
    return make_response(jsonify(extra_info.create(ExtraInfo.create_from_dto(content))), HTTPStatus.CREATED)


@extra_info_bp.get('/<int:extra_info_id>')
def get_description(extra_info_id: int) -> Response:
    return make_response(jsonify(extra_info.find_by_id(extra_info_id)), HTTPStatus.OK)


@extra_info_bp.put('/<int:extra_info_id>')
def update_description(extra_info_id: int) -> Response:
    content = request.get_json()
    extra_info.update(extra_info_id, ExtraInfo.create_from_dto(content))
    return make_response("ExtraInfo updated", HTTPStatus.OK)


@extra_info_bp.patch('/<int:extra_info_id>')
def patch_description(extra_info_id: int) -> Response:
    extra_info.patch(extra_info_id, request.get_json())
    return make_response("ExtraInfo updated", HTTPStatus.OK)


@extra_info_bp.delete('/<int:extra_info_id>')
def delete_description(extra_info_id: int) -> Response:
    extra_info.delete(extra_info_id)
    return make_response("ExtraInfo deleted", HTTPStatus.OK)
