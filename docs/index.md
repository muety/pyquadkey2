# Introduction
This is a feature-rich Python implementation of [QuadKeys](https://docs.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system), an approach to **geographical tiling**, that was proposed by Microsoft to be used for Bing Maps.

In essence, the concept is to **recursively** divide the flat, two-dimensional world map into squares. Each square contains **four squares** as children, which again contain four squares and so on, up **centimeter-level precision**. Each of these squares is **uniquely identifiable with a string** like `021030032`.

For more details on the concept, please refer to the [original article](https://docs.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system).

[n1try/pyquadkey2](https://github.com/n1try/pyquadkey2) originates from a **fork** of [buckhx/QuadKey](https://github.com/buckhx/QuadKey), which is not maintained anymore. It build on top of that project and adds:

* ✅ Several (critical) [bug fixes](https://github.com/buckhx/QuadKey/pull/15)
* ✅ Python 3 support
* ✅ [Type hints](https://docs.python.org/3.6/library/typing.html) for all methods
* ✅ Higher test coverage
* ✅ Cython backend for improved performance
* ✅ 64-bit integer representation of QuadKeys
* ✅ Additional features and convenience methods
