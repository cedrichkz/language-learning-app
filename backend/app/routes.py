from flask import Blueprint, jsonify, request

from .models import Card, db

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/cards", methods=["GET"])
def get_all_cards():
    cards = Card.query.order_by(Card.id).all()
    all_cards = [{"id":card.id, "front": card.front, "back": card.back} for card in cards]
    return jsonify(all_cards)


@api.route("/card/<int:card_id>", methods=["GET"])
def get_card_by_id(card_id):
    card = db.session.get(Card, card_id)
    if not card:
        return jsonify(error="card not found"), 404
    return jsonify(id=card.id, front=card.front, back=card.back)

@api.route("/card/<int:card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = db.session.get(Card, card_id)
    if not card:
        return jsonify(error="Card not found"), 404
    db.session.delete(card)
    db.session.commit()
    return jsonify(message="Card deleted"), 200

@api.route("/card", methods=["POST"])
def add_card():
    data = request.get_json() or {}
    front = data.get("front", "").strip()
    back = data.get("back", "").strip()

    if not front or not back:
        return jsonify(error="front and back are required"), 400
    card = Card(front=front, back=back)
    db.session.add(card)
    db.session.commit()
    return jsonify(id=card.id, front=card.front, back=card.back), 201