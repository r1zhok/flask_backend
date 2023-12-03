from .orders.film_controller import FilmController
from .orders.actor_controller import ActorController
from .orders.description_controller import DescriptionController
from .orders.extra_info_controller import ExtraInfoController
from .orders.film_has_rating_controller import FilmHasRatingController
from .orders.genre_controller import GenreController
from .orders.interesting_facts_controller import InterestingFactsController
from .orders.person_controller import PersonController
from .orders.rating_controller import RatingController
from .orders.review_controller import ReviewController
from .orders.review_has_film_controller import ReviewHasFilmController
from .orders.roles_controller import RolesController


film_controller = FilmController()
actor_controller = ActorController()
description_controller = DescriptionController()
extra_info_controller = ExtraInfoController()
film_has_rating_controller = FilmHasRatingController()
genre_controller = GenreController()
interesting_facts_controller = InterestingFactsController()
person_controller = PersonController()
rating_controller = RatingController()
review_controller = ReviewController()
review_has_film_controller = ReviewHasFilmController()
roles_controller = RolesController()