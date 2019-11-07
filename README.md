# 🌍 pyquadkey2
[![Documentation](https://docs.muetsch.io/badge.svg)](https://docs.muetsch.io/pyquadkey2/)

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

## Installation
### Requirements
This library requires **Python 3.6** or higher. To compile it by yourself, Cython is required in addition.

### Using Pip
* `pip3 install pyquadkey2`

Pip installation is only tested for Linux, yet. If you encounter problems with the installation on Mac or Windows, please report them as a new issue.

### From archive
* Download the latest [release](https://github.com/n1try/pyquadkey2/releases) as archive (`.tar.gz`) or wheel (`.whl`), e.g. `0.1.1.tar.gz`
* Install it with pip: `pip3 install 0.1.1.tar.gz`

### From source
* Clone repository: `git clone https://github.com/n1try/pyquadkey2`
* Make sure Cython is installed: `pip3 install cython`
* Compile Cython modules: `cd pyquadkey2/quadkey/tilesystem && python3 setup.py build_ext --inplace && ../../`
* Install the library with Pip: `pip3 install .`

### Troubleshooting
* `ImportError: cannot import name 'tilesystem'`: Simply try `pip3 install --upgrade pyquadkey2` once again. Second time usually works, as required build extensions are installed then. This is a known issue and will be fixed in the future.

## License
Apache 2.0

[![Buy me a coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoff.ee/n1try)
