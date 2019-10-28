# python3 setup.py build_ext --inplace

from distutils.core import setup
from distutils.extension import Extension

from Cython.Build import cythonize

setup(
    name='tilesystem',
    ext_modules=cythonize(
        Extension(
            'tilesystem',
            sources=['tilesystem.pyx'],
            include_dirs=[]
        )
    )
)
