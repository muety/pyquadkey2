#!/usr/bin/env python
# https://packaging.python.org/tutorials/packaging-projects/
import os

from setuptools import setup, find_packages
from setuptools.glob import glob

try:
    from Cython.Distutils.extension import Extension
    from Cython.Build import build_ext
except ImportError:
    from setuptools import Extension

    USING_CYTHON = False
else:
    USING_CYTHON = True

ext = 'pyx' if USING_CYTHON else 'c'
sources = glob('quadkey/tilesystem/*.%s' % (ext,))
extensions = [Extension(source.split('.')[0].replace(os.path.sep, '.'), sources=[source]) for source in sources]
cmdclass = {'build_ext': build_ext} if USING_CYTHON else {}

setup(
    name='pyquadkey2',
    version='0.1.0',
    description='Python implementation of geographical tiling using QuadKeys as proposed by Microsoft',
    author='Ferdinand Mütsch',
    author_email='ferdinand@muetsch.io',
    url='https://github.com/n1try/pyquadkey2',
    packages=find_packages(),
    project_urls={
        'Bug Tracker': 'https://github.com/n1try/pyquadkey2/issues',
        'Source Code': 'https://github.com/n1try/pyquadkey2',
    },
    keywords='tiling quadkey quadtile geospatial geohash',
    python_requires='>=3.6',
    ext_modules=extensions,
    cmdclass=cmdclass
)
