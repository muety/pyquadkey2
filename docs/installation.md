## Installation
### Requirements

This library requires **Python 3.10** or higher. To compile it from source, Cython is required in addition.

### Using Pip
```bash
$ pip install pyquadkey2
```

Pip installation is only tested for Linux and Mac, yet. If you encounter problems with the installation on Windows, please report them as a new issue.

### From archive
```bash
$ wget https://github.com/muety/pyquadkey2/releases/download/0.3.3/pyquadkey2-0.3.3.tar.gz
$ pip install pyquadkey2-0.3.3.tar.gz
```

### From source
#### Prerequisites (`Linux`)
* `gcc`
    * Fedora: `dnf install @development-tools`
    * Ubuntu / Debian: `apt install build-essential`
* `python3-devel`
    * Fedora: `dnf install python3-devel`
    * Ubuntu / Debian: `apt install python3-dev`
    * Others: See [here](https://stackoverflow.com/questions/21530577/fatal-error-python-h-no-such-file-or-directory/21530768#21530768)

#### Prerequisites (`Windows`)
* Visual C++ Build Tools 2015 (with Windows 10 SDK) (see [here](https://devblogs.microsoft.com/python/unable-to-find-vcvarsall-bat/#i-need-a-package-that-has-no-wheel-what-can-i-do))

#### Build
```bash
# Check out repo
$ git clone https://github.com/muety/pyquadkey2

# Create and active virtual environment (optional)
$ python -m venv ./venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Compile
$ cd src/pyquadkey2/quadkey/tilesystem && python setup.py build_ext --inplace && cd ../../../..

# Install as module
$ pip install .
```

## Developer Notes

### Build docs

```bash
pip install mkdocs
mkdocs build
```