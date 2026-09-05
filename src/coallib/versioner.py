#!/usr/bin/env python3
# Made by @Ericwasepic127


import sys
def pyVer():
    """Returns current version tuple"""
    return (
        sys.version_info.major, 
        sys.version_info.minor,
        sys.version_info.micro
    )

def moduleVer(module, fallback=(0,0,0)):
    """Gives module version from given module"""
    if hasattr(module, "__ver__"):
        tup = []
        for dight in module.__ver__:
            tup.append(int(dight)) if dight.isdigit() else None
        return tuple(tup)
    elif hasattr(module, "__version__"):
        tup = []
        for dight in module.__version__:
            tup.append(int(dight)) if dight.isdigit() else None
        return tuple(tup)
    else:
        if Version(pyVer()) > Version((3, 8)):
            from importlib.metadata import version
            tup = []
            try:
                ver = version(module.__name__)
            except:
                return fallback
            for dight in ver:
                tup.append(int(dight)) if dight.isdigit() else None
            return tuple(tup)
        else:
            return fallback

class Version(tuple):
    """Version object to be simple"""
    def __new__(self, value):
        if not isinstance(
            value,
            tuple
        ):
            raise TypeError(
                "Needs tuple, "
                f"not {type(value).__name__}"
            )
        if len(value) <= 1 or len(value) > 3:
            raise ValueError(
                "Got more "
                "or less argu"
                "ments than ex"
                "pected"
            )
        for item in value:
            if not isinstance(
                item,
                int
            ):
                raise ValueError(
                    "Version tuple"
                    " must be integer "
                    "including only, "
                    f"not {type(item).__name__}"
                )
        return super().__new__(self, value)
    
    def __repr__(self):
        return ".".join(
            [str(x) for x in self]
        )
        
    def __lt__(self, compare):
        if not isinstance(
            compare,
            Version
        ):
            raise TypeError(
                "Compare version"
                " using Version"
                " class, anything"
                " else won't work"
            )
        return tuple(
            self
        ) < tuple(
            compare
        )
        
    def __gt__(self, compare):
        return not self.__lt__(
            compare
        )
        
    def __le__(self, compare):
        if not isinstance(
            compare,
            Version
        ):
            raise TypeError(
                "Compare version"
                " using Version"
                " class, anything"
                " else won't work"
            )
        return tuple(
            self
        ) <= tuple(
            compare
        )
    
    def __ge__(self, compare):
        return not self.__le__(
            compare
        )
    
    def __eq__(self, compare):
        if not isinstance(
            compare,
            Version
        ):
            raise TypeError(
                "Compare version"
                " using Version"
                " class, anything"
                " else won't work"
            )
        return tuple(
            self
        ) == tuple(
            compare
        )
    def __ne__(self, compare):
        return not self.__eq__(
            compare
        )
