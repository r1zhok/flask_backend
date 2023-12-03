"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.film_route import film_bp
    from .orders.actor_route import actor_bp
    from .orders.review_route import review_bp
    from .orders.description_route import description_bp
    from .orders.extra_info_route import extra_info_bp
    from .orders.film_has_rating_route import film_has_rating_bp
    from .orders.genre_route import genre_bp
    from .orders.interesting_facts_route import interesting_facts_bp
    from .orders.rating_route import rating_bp
    from .orders.person_route import person_bp
    from .orders.review_has_film_route import review_has_film_bp
    from .orders.roles_route import role_bp

    app.register_blueprint(film_bp)
    app.register_blueprint(actor_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(description_bp)
    app.register_blueprint(extra_info_bp)
    app.register_blueprint(film_has_rating_bp)
    app.register_blueprint(genre_bp)
    app.register_blueprint(interesting_facts_bp)
    app.register_blueprint(rating_bp)
    app.register_blueprint(person_bp)
    app.register_blueprint(review_has_film_bp)
    app.register_blueprint(role_bp)
