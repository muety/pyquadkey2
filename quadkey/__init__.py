from util import precondition
from tile_system import TileSystem, valid_key

class QuadKey:

	@precondition(lambda c, key: valid_key(key))
	def __init__(self, key):
		"""
		A quadkey must be between 1 and 23 digits and can only contain digit[0-3]
		"""
		self.key = key 
		self.level = len(key)
		
	def is_parent(self, parent):
		return self != parent and parent.key[:len(self.key)-1] == self.key

	def __eq__(self, other):
		return self.key == other.key

	def __ne__(self, other):
		return not self.__eq__(other)

	def __str__(self):
		return self.key

	def __repr__(self):
		return self.key

	@staticmethod
	def from_geo(geo, level):	
		"""
		Constucts a quadkey representation from geo and level
		geo => (lat, lon)
		If lat or lon are outside of bounds, they will be clipped
		If level is outside of bounds, an AssertionError is raised
		
		"""
		pixel = TileSystem.geo_to_pixel(geo, level)
		tile = TileSystem.pixel_to_tile(pixel)
		key = TileSystem.tile_to_quadkey(tile, level)
		return QuadKey(key) 


