There are **three ways** of instantiating a QuadKey.

## From string representation
`from_str(qk_str: str) -> 'QuadKey'`

**Example:**
```
import quadkey
qk = quadkey.from_str('010302121')                  # -> 010302121
```

## From integer representation
`from_int(qk_int: int) -> 'QuadKey'`

**Example:**
```
import quadkey
qk = quadkey.from_int(1379860704579813385)          # -> 010302121
```