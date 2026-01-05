from util import precondition
from math import sin, cos, atan, exp, log, pi
from decimal import *

def valid_level(level):
	LEVEL_RANGE = (1,23)
	return LEVEL_RANGE[0] <= level <= LEVEL_RANGE[1]

getcontext().prec = 6

class TileSystem:
	"""
	Class with static method to build quadkeys from lat, lon, levels
	see http://msdn.microsoft.com/en-us/library/bb259689.aspx
	"""

	EARTH_RADIUS = 6378137
	LATITUDE_RANGE = (-85.05112878, 85.05112878)
	LONGITUDE_RANGE = (-180., 180.)

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
	@precondition(lambda lat, lvl: valid_level(lvl))
	def ground_resolution(lat, level):
		"""Gets ground res in meters / pixel"""
		lat = TileSystem.clip(lat, TileSystem.LATITUDE_RANGE)
		return cos(lat * pi / 180) * 2 * pi * TileSystem.EARTH_RADIUS / TileSystem.map_size(level)

	@staticmethod
	@precondition(lambda lat, lvl, dpi: valid_level(lvl))
	def map_scale(lat, level, dpi):
		"""Gets the scale of the map expressed as ratio 1	: N. Returns N"""
		return TileSystem.ground_resolution(lat, level) * dpi / 0.0254

	@staticmethod
	@precondition(lambda geo, lvl: valid_level(lvl))
	def geo_to_pixel(geo, level):
		"""Transform from geo coordinates to pixel coordinates"""
		lat, lon = float(geo[0]), float(geo[1])
		lat = TileSystem.clip(lat, TileSystem.LATITUDE_RANGE)
		lon = TileSystem.clip(lon, TileSystem.LONGITUDE_RANGE)
		x = (lon + 180) / 360
		sin_lat = sin(lat * pi / 180)
		y = 0.5 - log((1 + sin_lat) / (1 - sin_lat)) / (4 * pi)
		# might need to cast to uint
		map_size = TileSystem.map_size(level)
		pixel_x = int(TileSystem.clip(x * map_size + 0.5, (0, map_size - 1)))
		pixel_y = int(TileSystem.clip(y * map_size + 0.5, (0, map_size - 1)))
		# print '\n'+str( ((lat, lon), sin_lat, (x, y), map_size, (pixel_x, pixel_y)) )+'\n'
		return pixel_x, pixel_y

	@staticmethod
	@precondition(lambda pix, lvl: valid_level(lvl))
	def pixel_to_geo(pixel, level):
		"""Transform from pixel to geo coordinates"""
		pixel_x = pixel[0]
		pixel_y = pixel[1]
		map_size = float(TileSystem.map_size(level))
		x = (TileSystem.clip(pixel_x, (0, map_size - 1)) / map_size) - 0.5
		y = 0.5 - ( TileSystem.clip(pixel_y, (0, map_size - 1)) / map_size)
		lat = 90 - 360 * atan(exp(-y * 2 * pi)) / pi
		lon = 360 * x
		return round(lat,6), round(lon,6)

	@staticmethod
	def pixel_to_tile(pixel):
		"""Transform pixel to tile coordinates"""
		return pixel[0] / 256, pixel[1] / 256

	@staticmethod
	def tile_to_pixel(tile):
		"""Transform tile to pixel coordinates"""
		return tile[0] * 256, tile[1] * 256

	@staticmethod
	@precondition(lambda tile, lvl: valid_level(lvl))
	def tile_to_quadkey(tile, level):
		"""Transform tile coordinates to a quadkey"""
		tile_x = tile[0]
		tile_y = tile[1]
		quadkey = ""
		for i in xrange(level):
			bit = level - i
			digit = ord('0')
			mask = 1 << (bit - 1) #if (bit - 1) > 0 else 1 >> (bit - 1)
			if (tile_x & mask) is not 0:
				digit += 1
			if (tile_y & mask) is not 0:
				digit += 2
			quadkey += chr(digit)
		return quadkey

	@staticmethod
	def quadkey_to_tile(quadkey):
		"""Transform quadkey to tile coordinates"""
		pass
	
