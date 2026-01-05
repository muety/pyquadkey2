# Installation

## Requirements
This library requires **Python 3.6** or higher. To compile it by yourself, Cython is required in addition.

## Using Pip
* `pip3 install pyquadkey2`

If you encounter problems while installing, please report them as a new issue.

## From archive
* Download the latest [release](https://github.com/n1try/pyquadkey2/releases) as archive (`.tar.gz`) or wheel (`.whl`), e.g. `0.1.1.tar.gz`
* Install it with pip: `pip3 install 0.1.1.tar.gz`

## From source
* Clone repository: `git clone https://github.com/n1try/pyquadkey2`
* Make sure Cython is installed: `pip3 install cython`
* Compile Cython modules: `cd pyquadkey2/quadkey/tilesystem && python3 setup.py build_ext --inplace && ../../`
* Install the library with Pip: `pip3 install .`

## Troubleshooting
* `ImportError: cannot import name 'tilesystem'`: Simply try `pip3 install --upgrade pyquadkey2` once again. Second time usually works, as required build extensions are installed then. This is a known issue and will be fixed in the future.
