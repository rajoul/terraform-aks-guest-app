from app import database


class Guest(database.Model):
    """Simple database model to track event attendees."""

    __tablename__ = 'guests'
    id = database.Column(database.Integer, primary_key=True)
    first_name = database.Column(database.String(80))
    last_name = database.Column(database.String(80))
    email = database.Column(database.String(120))
    group_size = database.Column(database.Integer, default=1)
    meal_option = database.Column(database.String(80))

    def __init__(self, first_name=None, last_name=None, email=None, group_size=1, meal_option="vegetarian"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.group_size = group_size
        self.meal_option = meal_option
