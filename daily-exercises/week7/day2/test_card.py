from cards import Card


def test_create_card():
	card = Card()
	assert isinstance(card, Card)
