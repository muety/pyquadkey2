QuadKey
=======

Quad key object used for Geospatial segmentation. Based off the idea of a quadtree and used as the Bing Maps tile system.

Given a (lat, lon) and level produce a quadkey to be used in Bing Maps.
Can also supply methods to generate a Google Maps TileXYZ

Built off of the TileSystem static class outlined here: http://msdn.microsoft.com/en-us/library/bb259689.aspx

Converts a lat,lon to pixel space to tile space to a quadkey 


		import quadkey

		qk = quadkey.from_geo((-105, 40), 17)
		print qk.key # => 02310101232121212 
		assert qk.level is 17
		tile = qk.to_tile() # => [(x, y), z]

Not a lot of documentation here, but the implementation has quite a bit, so look at the QuadKey definitions for better documention
