#!/usr/bin/env python3
# Made by @Ericwasepic127

import itertools

class Dummy:
     def __getattr__(self, name):
        return Dummy()
     def __setattr__(self, name, value):
        pass
     def __delattr__(self, name):
        pass
     def __getitem__(self, name):
        return Dummy()
     def __setitem__(self, name, value):
        pass
     def __delitem__(self, name):
        pass
     def __iter__(self):
        return itertools.cycle([Dummy()])
     def __repr__(self):
        return "<Dummy>"
     def __eq__(self, obj):
        return True
     def __gt__(self, obj):
        return True
     def __lt__(self, obj):
        return True
     def __call__(self, *args, **kwargs):
        return Dummy()
     def __enter__(self, *__, **_):
        return self
     def __exit__(self, *a, **k):
        return not bool(a)

def Lambda(defaultArgs: tuple=(), defaultKwargs: dict={}) -> object:
    getArgs = bool(defaultArgs or defaultKwargs)
    def wrapper(func):
        if not getArgs:
            def w(*arg, **kwarg):
                a = arg or defaultArgs
                k = kwarg or defaultKwargs
                return func(*a, **k)
        else:
            def w():
                return func(*default)
        return w
    return wrapper
