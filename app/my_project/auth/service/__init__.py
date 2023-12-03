"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.film_service import FilmService
from .orders.actor_service import ActorService

client_service = FilmService()
client_type_service = ActorService()
