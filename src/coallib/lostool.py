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

def custom_repr(name_to=None):
    """Custom REPR-ing at function"""
    if not isinstance(name_to, str):
        name_to = "<Function %s>"
    def wrap(func):
        class CustomRepr:
            def __repr__(self):
                return (name_to % func.__name__) if "%s" in name_to else name_to
            def __call__(self, *a, **k):
                return func(*a, **k)
        CustomRepr.__call__.__doc__ = func.__doc__
        return CustomRepr()
    return wrap(name_to) if callable(name_to) else wrap

def smartDeco(defArg=(), defKwarg={}):
    """Smart decorater"""
    def helper(deco):
        def wrapper(*args, **kwargs):
            res = deco(*defArg, **defKwarg)(args[0]) if len(args) == 1 and callable(args[0]) and not kwargs else deco(*args, **kwargs)
            return res
        return wrapper
    return helper
