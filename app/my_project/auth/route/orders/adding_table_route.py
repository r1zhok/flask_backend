from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify, request
from my_project.auth.controller.orders import adding_table_controller
from my_project.auth.domain.orders.additional_table import AdditionalTable

adding_table_bp = Blueprint('adding_table', __name__, url_prefix='/adding_table')
adding_table = adding_table_controller.AddingTableController()


@adding_table_bp.get('')
def get_all_adding() -> Response:
    return make_response(jsonify(adding_table.find_all()), HTTPStatus.OK)


@adding_table_bp.post('')
def create_adding() -> Response:
    content = request.get_json()
    return make_response(jsonify(adding_table.create(AdditionalTable.create_from_dto(content))), HTTPStatus.CREATED)


@adding_table_bp.get('/<int:adding_table_id>')
def get_adding(adding_table_id: int) -> Response:
    return make_response(jsonify(AdditionalTable.find_by_id(adding_table_id)), HTTPStatus.OK)


@adding_table_bp.put('/<int:adding_table_id>')
def update_adding(adding_table_id: int) -> Response:
    content = request.get_json()
    adding_table.update(adding_table_id, AdditionalTable.create_from_dto(content))
    return make_response("ExtraInfo updated", HTTPStatus.OK)


@adding_table_bp.patch('/<int:adding_table_id>')
def patch_adding(adding_table_id: int) -> Response:
    adding_table.patch(adding_table_id, request.get_json())
    return make_response("ExtraInfo updated", HTTPStatus.OK)


@adding_table_bp.delete('/<int:adding_table_id>')
def delete_adding(adding_table_id: int) -> Response:
    adding_table.delete(adding_table_id)
    return make_response("ExtraInfo deleted", HTTPStatus.OK)
