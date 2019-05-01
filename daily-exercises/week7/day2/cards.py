import random


class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def get_name(self):
		if self.value == 1:
			return 'ace'
		elif self.value == 11:
			return 'jack'
		elif self.value == 12:
			return 'queen'
		elif self.value == 13:
			return 'king'
		else:
			return str(self.value)

	def __str__(self):
		name = self.get_name()
		return "{} of {}".format(name, self.suit)

	def __repr__(self):
		return self.__str__()

class Deck:
	def __init__(self):
		self.cards = []
		for suit in ('hearts', 'spades', 'diamonds', 'clubs'):
			for value in range(1, 13 + 1):
				card = Card(value, suit)
				self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)

	def add(self, cards):
		for card in cards:
			self.cards.append(card)

	def draw(self, amount):
		if amount > len(self.cards):
			amount = len(self.cards)

		to_draw = []
		for i in range(amount):
			card = self.cards.pop()
			to_draw.append(card)
		return to_draw


class Hand(Deck):
	def __init__(self):
		self.cards = []