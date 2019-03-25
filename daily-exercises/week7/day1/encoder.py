import random


class Encoder:

	KEYS   = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ., 0123456789-_'
	VALUES = 'UG9wS24joQrB0Nu_nOPavIJ8cm d1lZRtykC.A7bWYh-3qzF5XHKLgpViDMeTE,6sxf'

	def get_map(self):
		mapped = dict(zip(self.KEYS, self.VALUES))
		return mapped

	def get_reverse_map(self):
		mapped = dict(zip(self.VALUES, self.KEYS))
		return mapped

	def encode(self, message):
		mapped = self.get_map()
		encoded = ''
		for letter in message:
			encoded += mapped[letter]
		return encoded

	def decode(self, message):
		mapped = self.get_reverse_map()
		decoded = ''
		for letter in message:
			decoded += mapped[letter]
		return decoded
