#!/usr/bin/env python3
# Made by @Ericwasepic127
"""
loady - Loading Bar simulator!
Use for loading! 
Fun loads including!
Get and use! 
Simple! 
"""
# loady.py
from time import sleep as sl
from random import choice as ch
from itertools import cycle as cy
from traceback import print_exc as pe
from threading import Thread as th

class ForceTerminated(Exception):
    """Loady's spinFunc terminated exception"""

try:
    from ctypes import pythonapi
    import ctypes
    _pt = pythonapi.PyThreadState_SetAsyncExc
    def pt(thread):
        """Try to force-terminate thread given"""
        th_id = ctypes.c_long(thread.ident)
        exc = ctypes.py_object(ForceTerminated)
        res = _pt(th_id, exc)
        if res == 0:
            return False
        elif res > 1:
            _pt(th_id, 0)
            return False
        return True
    del pythonapi
except:
    import sys
    print("[WARNING]: cannot force-terminate in spinFunc", file=sys.stderr)
    pt = None

def loadBar(icon="#", left=".", long=25, sleeps=0.1):
    """
    Regular loading bar
    Arguments: 
        icon='#' - What should display if increases 
        left=" ." - What display left items
        long=25 - How longs 
        sleeps=0.1 - How long between loads
    """
    level = long - 1
    for a in range(long):
        dashes = icon * a
        spaces = left * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(sleeps)
    print()

def randomChapter(icon="0123456789", left=" .", long=25, sleeps=0.1):
    """
    Randomly selects from icon, then increase 
    Arguments: 
        icon='0123456789' - What should display if increases 
        left=". " - What display left items
        long=25 - How long
        sleeps=0.1 - How long between loads
    """
    level = long - 1
    for a in range(long):
        dashes = ch(icon) * a
        spaces = left * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(sleeps)
    print()

def conituner(icon="0123456789", left=" .", long=10, sleeps=0.1):
    """
    Loops from icon, increase 
    Arguments: 
        icon='0123456789' - What should display if increases 
        left=". " - What display left items
        long=10 - How longs 
        sleeps=0.1 - How long between loads
    """
    ico = cy(iter(icon))
    level = long - 1
    for a in range(long):
        dashes = next(ico) * a
        spaces = left * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(sleeps)
    print()

def decrase(icon="#", left=" .", long=25, sleeps=0.1):
    """
    Reversed loads
    Arguments: 
        icon=''#" - What should display if decreases 
        left=". " - What display left items
        long=25 - How longs 
        sleeps=0.1 - How long between loads
    """
    level = long - 1
    for a in range(long):
        dashes = left * a
        spaces = icon * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(sleeps)
    print()

def between(icon="#", left=".", long=25, sleeps=(0.5, 0.1, 1, 3)):
    """
    Randomly selects from sleep range, then sleeps
    Arguments: 
        icon='#' - What should display if increases 
        left=" ." - What display left items
        long=25 - How long
        sleeps=(0.5, 0.1, 1, 3) - How long between loads
    """
    level = long - 1
    for a in range(long):
        dashes = icon * a
        spaces = left * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(ch(sleeps))
    print()

def loadFunc(icon="#", left=".", long=25, run={}, showError=False):
    """
    Loads with function, becoming real!
    Arguments: 
        icon='#' - What should display if increases 
        left=" ." - What display left items
        long=25 - How long
        run={} - A dictonary like this format: {"Title, meaning, what is doing": function_to_run}
        showError=False - If true, then raises; If false, then breaks and errors tracebacked (no raising)
    """
    if type(run) != dict:
        raise TypeError(f"'run' must dict, not {type(run).__name__!r}")
    if not run:
        return
    per = 100 / len(run.keys())
    current = 0
    success = True
    for title, function in run.items():
        calc = int((current / 100) * long)
        string = f"[{icon*calc}{left*(long - calc)}] {int(current)}%: {title}"
        print(string, end="\r")
        try:
            function()
        except:
            print(f"Error occured during {title}:")
            success = False
            if showError:
                raise
            else:
                pe()
                break
        current += per
    print() if success else None
    
class Spinner(cy):
    """Must use this to convert your list into usable loady.spinFunc mode"""
    def __repr__(self):
        return f"<loady.spinFunc mode (usable) animation>"
DEFAULT_SPIN = Spinner(["/", "-", "\\", "|"])

def spinFunc(mode=DEFAULT_SPIN, run=None, timeout=0, info="Loading", end="done"):
    """
    Loads with Rotation animation by Unicode chapters!
    Arguments:
        mode=loady.DEFAULT_SPIN - Animation object; (WARNING: You must give loady.Spinner object to your custom animation)
        run=None - What function will run
        timeout=0 - if it's zero or below, no timeout; Above 0 means how much seconds will it wait
        info="Loading" - Info message
        end="done" - End message
    """
    if type(mode) != Spinner:
        raise TypeError(f"'mode' must be loady.Spinner, not {type(mode)}")
    if run is None:
        return
    if type(end) != str:
        raise TypeError(f"'end' must be str, not {type(timeout)}")
    if type(info) != str:
        raise TypeError(f"'info' must be str, not {type(timeout)}")
    if type(timeout) != int:
        raise TypeError(f"'timeout' must be int, not {type(timeout)}")
    terminate = True
    if timeout < 1:
        timeout = -1
        terminate = False
    func_thread = th(daemon=True, target=run)
    func_thread.start()
    
    time_temp = 0
    for animation in mode:
        if timeout and func_thread.is_alive():
            if time_temp == 10:
                time_temp = 0
                timeout -= 1
            else:
                time_temp += 1
            print(f"{info} {animation}", end="\r", flush=True)
            sl(0.1)
        else:
            break
    if terminate:
        if pt is None:
            print(f"{info} cannot force-terminate, waiting until finish with timeout", flush=True, end="\r")
            func_thread.join(timeout)
            print(info, end, " "*57 - len(end))
        else:
            print(f"{info} timeout reached", end="\r", flush=True)
            if not pt(func_thread):
                print(f"{info} cannot force-terminate, waiting until finish with timeout", end="\r")
                func_thread.join(timeout)
                print(info, end, " "*(57 - len(end)))
            else:
                print(info, end, " "*(15 - len(end)))
    else:
        print(info, end)

__all_dict__ = {
    "loadFunc": loadFunc,
    "loadBar": loadBar, 
    "randomChapter": randomChapter, 
    "conituner": conituner, 
    "decrase": decrase, 
    "between": between,
    "Spinner": Spinner,
    "spinFunc": spinFunc
}
__all__ = list(__all_dict__.keys())
__version__ = "V1.1"
