#!/usr/bin/env python3
# Made by @Ericwasepic127

"""
Functions to make if statements smaller
Made by @Ericwasepic127, Licensed under MIT
"""

def check_type(obj, classCheck):
    """Check instances"""
    return isinstance(obj, classCheck) or type(obj) == classCheck

def raise_type(obj, classCheck, where="<unknown>", exc=TypeError, explain=None):
    """Raises exc (kwarg) exception when obj attribute (1st argument) is not inherted from classCheck (2nd attribute)
    Arguments:
       POS 1: obj - Object to check
       POS 2: classCheck - Class of 1st arguments's should match or Inherted/Subclassed/Instanced from it
       POS 3: where="<unknown>" - String argument to say in function's what argument was invaild
       POS 4: exc=TypeError - Exception to raise
       POS 5: explain=None - Exception message, defaults to f"argument {where} must {classCheck.__name__!r}, got {obj.__name__!r}"
    Epilog:
        def multipy(num):
            coallib.raise_type(num, int, where='num')
            return num * 2
        # This function only gets integer, if not given integer, it raises as
        # TypeError: argument num must 'int', got 'str'
        # when you do multipy('test')"""
    if explain is None or not explain:
        explain = f"argument {where} must {classCheck.__name__!r}, got {obj.__name__!r}"
    if not check_type(obj, classCheck):
        raise exc(explain)

def raise_callable(obj, where="<unknown>", exc=TypeError, explain=None):
        """Raises exc (kwarg) exception when obj attribute (1st argument) is not callable
    Arguments:
       POS 1: obj - Object to check
       POS 2: where="<unknown>" - String argument to say in function's what argument was invaild
       POS 3: exc=TypeError - Exception to raise
       POS 4: explain=None - Exception message, defaults to f"argument {where} must {classCheck.__name__!r}, got {obj.__name__!r}"
    Epilog:
        def wrapper(func):
            coallib.raise_callable(func, where='num')
            def wrap():
              return func()
            return wrap
        # This wrapper only gets functions, if not it raises as
        # TypeError: argument num must callable, got 'str'
        # when you do wrapper('test')"""
    if explain is None or not explain:
        explain = f"argument {where} must callable, got {obj.__name__!r} object"
    if not callable(obj) or not hasattr(obj, "__call__"):
        raise exc(explain)
