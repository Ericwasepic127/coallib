#!/usr/bin/env python3
# Made by @Ericwasepic127

"""
Helps to pyscript
"""

__all__ = ["worker_base_path", "fetch", "SLD"]

from pyscript import storage as s
from asyncio import run as asynch
from random import choice as c
from pyodide.ffi import can_run_sync A cRs
import asyncio, pyscript, time

def worker_base_path(loc: str) -> str:
    """Helps path to fix in worker, which when try ./examplefile, it tries to blob URL and fails"""
    return js.location.origin + loc

def fetch(url, slient=False, mode="t"):
    """Gets text from website, then return
    You can get bytes from the URL, add mode="b" to it! Anything else on mode will give you text/str
    You can do things slient/no verbose, just set slient=True"""
    try:
        it = a(pyscript.fetch(url))
        if it.ok:
            if mode == "b":
                re = bytes(a(it.bytes()))
            else:
                re = a(it.text())
        else: 
            print(f"Something went wrong when fetching URL {url}! Status code: {it.status}", file=sys.stderr) if not slient else None
            re = None
        return re
    except (BaseException, Exception) as e:
        print(f"Something went wrong when fetching URL {url}! Error: {e}", file=sys.stderr) if not slient else None
        return None

def runSync(coroutine):
    """Awaits coroutine"""
    try:
        if cRs():
            return asynch(coroutine)
    except (BaseException, Exception) as e:
        if "stack" in str(e).lower():
            pass
        else:
            raise
        async def coro_wrap():
            try:
                return False, await coroutine
            except (BaseException, Exception) as e:
                return True, e

            coro = asyncio.create_task(coro_wrap)
            while not coro.done():
                time.sleep(.0825)
            status, info = coro.result()
            if status:
                raise info
            return info

a = runSync

class SLD:
    def __init__(self, name=None):
        if name is None:
            q = "qwertyuiopasdfghjklzxcvbnm1234567890"
            name = "".join([c(q) for _ in "-"*6])
        self.name = name
        self.storage = a(s(name))
        def __repr__(self):
            return f"<pyscript.storage (SLD): {self.name}>"
        def sync(self):
            """Synchronization"""
            a(self.storage.sync())
        def save(self, name, item):
            """Saves item to persistent storage"""
            self.storage[name] = item
            self.sync()
        def load(self, name):
            """Loads item from persistent storage"""
            self.sync()
            return self.storage.get(name)
        def delete(self, name):
            """Deletes item from persistent storage"""
            if name in self.storage.keys():
                del self.storage[name]
                self.sync()
            else:
                 raise KeyError(f"Key {name} doesn't exist!")
        def __getitem__(self, name):
            return self.load(name)
        def __delitem__(self, name):
            self.delete(name)
        def __setitem__(self, name, value):
            self.save(name, value)
