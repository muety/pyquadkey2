# Instantiation

There are **three ways** of instantiating a QuadKey.

## From string representation
Creates a new `QuadKey` object from a tile's string representation.

`from_str(qk_str: str) -> 'QuadKey'`

**Example:**
```python
from pyquadkey2 import quadkey
qk = quadkey.from_str('010302121')                  # -> 010302121
```

## From integer representation
Creates a new `QuadKey` object from a tile's integer representation

`from_int(qk_int: int) -> 'QuadKey'`

**Example:**
```python
from pyquadkey2 import quadkey
qk = quadkey.from_int(1379860704579813385)          # -> 010302121
```

## From coordinates
Creates a new `QuadKey` object from WGS 84 lat/lon coordinates

`from_geo(geo: Tuple[float, float], level: int) -> 'QuadKey'`

**Example:**
```python
from pyquadkey2 import quadkey
qk = quadkey.from_geo((49.011011, 8.414971), 9)     # -> 120203233
```