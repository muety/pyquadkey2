from util import precondition
from math import cos

class TileSystem:
	"""
	Class with static method to build quadkeys from lat, lon, levels
	see http://msdn.microsoft.com/en-us/library/bb259689.aspx

	"""

	EARTH_RADIUS = 6378137
	LATITUDE_RANGE = (-85.05112878, 85.05112878)
	LONGITUDE_RANGE = (-180., 180.)
	LEVEL_RANGE = (1,23)

	valid_level = lambda level: TileSystem.LEVEL_RANGE[0] <= level <= TileSystem.LEVEL_RANGE[1]

	@staticmethod
	@precondition(lambda n, minMax: minMax[0] <= minMax[1])
	def clip(n, minMax):
		"""	Clips number to specified values """
		return min(max(n, minMax[0]), minMax[1])

	@staticmethod
	@precondition(valid_level)
	def map_size(level):
		"""Determines map height and width in pixel space at level"""
		return 256 << level

	@staticmethod
	@precondition(valid_level(*args[1]))
	def ground_resolution(float lat, int level):
		"""Gets ground res in meters / pixel"""
		lat = TileSystem.clip(lat, TileSytem.LATITUDE_RANGE)
		return cos(lat * pi / 180) * 2 * pi * EARTH_RADIUS / TileSystem.map_size(level)

	@staticmethod
	@precondition(valid_level(*args[1]))
	def map_scale(lat, level, dpi):
		"""Gets the scale of the map expressed as ratio 1	: N. Returns N"""
		return TileSystem.ground_resolution(lat, level) * dpi / 0.0254

