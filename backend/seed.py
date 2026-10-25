# create a dict with one word
# feed it into the database

from app import create_app
from app.models import db, Card

app = create_app()

with app.app_context():
    if Card.query.first():
        print("Already seeded. Doing nothing.")
    else:
        db.session.add(Card(front="tommorow", back="manana"))
        db.session.commit()
        print("Seeded 1 card.")