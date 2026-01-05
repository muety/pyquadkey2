#!/usr/bin/env python
# https://packaging.python.org/tutorials/packaging-projects/
# pip install wheel auditwheel
# python setup.py sdist bdist_wheel
# python auditwheel repair -w dist/manylinux dist/pyquadkey2-0.2.2-cp39-cp39-linux_x86_64.whl  # <-- update lib- and python versions heree
# python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*.tar.gz dist/*win_*.whl dist/manylinux/*.whl
# mkdocs build

from setuptools import Extension
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pyquadkey2',
    version='0.3.2',
    description='Python implementation of geographical tiling using QuadKeys as proposed by Microsoft',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ferdinand Mütsch',
    author_email='ferdinand@muetsch.io',
    url='https://github.com/muety/pyquadkey2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Cython',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: GIS',
        'Typing :: Typed'
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/muety/pyquadkey2/issues',
        'Source Code': 'https://github.com/muety/pyquadkey2',
        'Documentation': 'https://docs.muetsch.io/pyquadkey2/'
    },
    keywords='tiling quadkey quadtile geospatial geohash',
    python_requires='>=3.10',
    ext_modules=[Extension('tilesystem', ['src/pyquadkey2/quadkey/tilesystem/tilesystem.c'])],
    ext_package='pyquadkey2'
)
