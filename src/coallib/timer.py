#!/usr/bin/env python3
# Made by @Ericwasepic127
"""JS like setTimeout"""
import time, asyncio
def timer(seconds, ms=False):
    """Timer as like JS's setTimeout, whatever"""
    if ms:
        seconds = seconds / 1000
    def wrap(func):
        async def _timer(*a, **k):
            async def wait():
                await asyncio.sleep(seconds)
                await asyncio.to_thread(lambda: func(*a, **k))
            async def listen():
                while not _timer.stop:
                    await asyncio.sleep(.1)
            f = asyncio.create_task(listen())
            w = asyncio.create_task(wait())
            done, pending = await asyncio.wait([f, w], return_when=asyncio.FIRST_COMPLETED)
            if w in done:
                if w.exception():
                    q = (False, w.exception())
                else:
                    q = (True, w.result())
            else:
                q = (False, KeyboardInterrupt())
            for task in pending:
                task.cancel()
            if q[0]:
                return q[1]
            else:
                raise q[1]
        _timer.stop = False
        return _timer
    return wrap
     
@timer(5)
def test():
    print("Waited for 5 seconds")

def run(coro, poll=0.1):
    """Run coroutine by polled loop"""
    task = task(coro)
    while not task.done():
        time.sleep(poll)
    return task

def task(coro):
    """Makes task, which run coroutine in background"""
    return asyncio.create_task(coro)
