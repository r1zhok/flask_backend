from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders import description_controller
from my_project.auth.domain.orders.description import Description

description_bp = Blueprint('descriptions', __name__, url_prefix='/descriptions')
description = description_controller.DescriptionController()


@description_bp.get('')
def get_all_descriptions() -> Response:
    return make_response(jsonify(description.find_all()), HTTPStatus.OK)


@description_bp.post('')
def create_description() -> Response:
    content = request.get_json()
    return make_response(jsonify(description.create(Description.create_from_dto(content))), HTTPStatus.CREATED)


@description_bp.get('/<int:description_id>')
def get_description(description_id: int) -> Response:
    return make_response(jsonify(description.find_by_id(description_id)), HTTPStatus.OK)


@description_bp.put('/<int:description_id>')
def update_description(description_id: int) -> Response:
    content = request.get_json()
    description.update(description_id, Description.create_from_dto(content))
    return make_response("Description updated", HTTPStatus.OK)


@description_bp.patch('/<int:description_id>')
def patch_description(description_id: int) -> Response:
    description.patch(description_id, request.get_json())
    return make_response("Description updated", HTTPStatus.OK)


@description_bp.delete('/<int:description_id>')
def delete_description(description_id: int) -> Response:
    description.delete(description_id)
    return make_response("Description deleted", HTTPStatus.OK)
