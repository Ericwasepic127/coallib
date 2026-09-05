#!/usr/bin/env python3
# Made by @Ericwasepic127

from . import loady, itertool, lostool, iftool, filetool, termtool, versioner, animlib, timer
import platform

imports = [loady, itertool, lostool, versioner, iftool, filetool, animlib, timer]

if "wasm32" in platform.architecture():
    from . import pyscripter, pagerfix, m2w
    imports.append(pyscripter, pagerfix, m2w)

every = []
for mod in imports:
    if hasattr(mod, "__all__"):
        every.append(mod.__all__)
    else:
        every.append(dir(mod))

__all__ = []
for x in every:
    for y in x:
        if y in __all__:
            raise RuntimeError(f"Imports are conflicting: {y} {x}")
        __all__.append(y) if not y.startswith("_") else None
__version__ = "V1.0"

def __getattr__(name):
    for mod in imports:
        if hasattr(mod, name):
            return getattr(mod, name)
    raise AttributeError(f"module 'ericutils' has no attribute {repr(name)}")

del platform, every
