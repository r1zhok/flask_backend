"""
2023
oleksii.strizhyk.ir.2022@lpnu.ua
© Oleksii Strizhyk
"""
from my_project import db
from my_project.auth.dao.orders import film_dao
from my_project.auth.domain import Film
from my_project.auth.service.general_service import GeneralService


class FilmService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = film_dao.FilmDAO()

