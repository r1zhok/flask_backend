from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

films_and_persons = Blueprint('films/persons', __name__, url_prefix='/films/persons')

@films_and_persons.get('')
def get_all_films_and_persons() -> Response:

