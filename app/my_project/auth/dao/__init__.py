from .orders.film_dao import FilmDAO
from .orders.actor_dao import ActorDAO
from .orders.extra_info_dao import ExtraInfoDAO
from .orders.description_dao import DescriptionDAO
from .orders.interesting_facts_dao import InterestingFactsDAO
from .orders.film_has_rating_dao import FilmHasRatingDAO
from .orders.genre_dao import GenreDAO
from .orders.person_dao import PersonDAO
from .orders.rating_dao import RatingDAO
from .orders.review_dao import ReviewDAO
from .orders.review_has_film_dao import ReviewHasFilmDAO
from .orders.roles_dao import RolesDAO

film_dao = FilmDAO()
client_type_dao = ActorDAO()
extra_info_dao = ExtraInfoDAO()
description_dao = DescriptionDAO()
interesting_facts_dao = InterestingFactsDAO()
film_has_rating_dao = FilmHasRatingDAO()
genre_dao = GenreDAO()
person_dao = PersonDAO()
rating_dao = RatingDAO()
review_dao = ReviewDAO()
review_has_film_dao = ReviewHasFilmDAO()
roles_dao = RolesDAO()
