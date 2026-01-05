QuadKey
=======

Quad key object used for Geospatial segmentation

		from quadkey import QuadKey

    qk = QuadKey((-105, 40) 17)
		print qk.key # => 02310101232121212 
		assert qk.level is 17
		copy = QuadKey.from_str(qk.key)
