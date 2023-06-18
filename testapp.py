from flask import current_app
from restaurant.models import Menu
from restaurant import db

with current_app.app_context():
    menu = Menu.query.get(3)
    menu.priceperunit = 5.60
    db.session.commit()