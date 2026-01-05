from util import precondition
from tile_system import TileSystem

class QuadKey:

	def __init__(self, lat, lon, level):
		# assert lat, lon and level are valid
		self.key = QuadKey.get_quadkey(lat, lon, level)
		self.lat = lat
		self.lon = lon
		self.level = level

	def __str__(self):
		return self.key

	def __repr__(self):
		return self.key

	@classmethod
	@precondition(TileSystem.valid_level)
	def from_str(cls, key):
		level = len(key)
		lat, lon = QuadKey.get_coordinates(key)
		return cls(lat, lon, level)

	@staticmethod
	def get_quadkey(lat, lon, level):	
		pass

	@staticmethod
	def get_coordinates(key):
		pass

