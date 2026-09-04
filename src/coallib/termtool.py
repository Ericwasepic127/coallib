#!/usr/bin/env python3
# Made by @Ericwasepic127

from .iftool import raise_type, raise_callable
from .itertool import full_fix_str as fixer

modes = {
    0: ("y*", "(y/n)"),
    1: ("ok", "(ok/cancel)"),
    2: ("s*", "(s/a)")
}

def add_mode(confirm, value):
    """Adds mode"""
    raise_type(value, tuple, where="value")
    modes[name] = value

class Modes:
    """Mode type"""
    def __init__(self,  mode=0):
        self.mode = modes[mode]

MODE_YN = Modes(0)
MODE_OK = Modes(1)
MODE_SA = Modes(2)

def confirm(prompt, mode=MODE_YN, use=input):
    """Confirming function: Give Modes object or by MODE_YN"""
    raise_type(mode,  Modes, where="mode")
    raise_callable(use, where="use")
    get = None
    ask = mode.mode
    asteirk = False
    if ask[0].endswith("*"):
        asteirk = True
        ask[0].strip("*")
    while get is None:
        try:
            user = fixer(use(f"{prompt} {ask[1]} ").lower())
        except:
            print("\n[WARNING]: Interrupted\n")
            continue
        if asteirk:
            get = user.startswith(ask[0])
        else:
            get = user == ask[0]
    return get
            
