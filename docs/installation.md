## Requirements
This library requires **Python 3.6** or higher. To compile it by yourself, Cython is required in addition.

## Using Pip
* `pip3 install pyquadkey2`

Currently, there are pre-built `linux_x86_64` for Python 3.6, 3.7 and 3.8. If you're on a Linux system, you can simply use pip without any additional requirements.
On other systems, you might need to install Cython first (`pip3 install cython`). If you encounter problems while installing, please report them as a new issue.

## From Source
* `git clone https://github.com/n1try/pyquadkey2`
* `pip3 install cython`
* `cd pyquadkey2/quadkey/tilesystem && python3 setup.py build_ext --inplace && ../../`
* `pip3 install .`

## Troubleshooting
* `ImportError: cannot import name 'tilesystem'`: Simply try `pip3 install --upgrade pyquadkey2` once again. Second time usually works, as required build extensions are installed then. This is a known issue and will be fixed in the future.