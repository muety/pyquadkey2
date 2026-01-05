#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
      name='pyquadkey2',
      version='0.1.0',
      description='Python implementation of geographical tiling using QuadKeys as proposed by Microsoft',
      author='Ferdinand Mütsch',
      author_email='ferdinand@muetsch.io',
      url='https://github.com/n1try/pyquadkey2',
      packages=find_packages(),
      install_requires=['Cython>=0.29.12'],
      project_urls={
            'Bug Tracker': 'https://github.com/n1try/pyquadkey2/issues',
            'Source Code': 'https://github.com/n1try/pyquadkey2',
      },
      keywords='tiling quadkey quadtile geospatial geohash'
)
