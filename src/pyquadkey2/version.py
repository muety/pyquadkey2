try:
    from ._version import __version__
except ImportError:
    import sys
    from importlib.metadata import version, PackageNotFoundError

    try:
        __version__ = version("pyquadkey2")
    except PackageNotFoundError:
        __version__ = "unknown"
