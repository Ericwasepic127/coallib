#!/usr/bin/env python3
# Made by @Ericwasepic127

'''
File: coallib/animlib.py
Author: Ericwasepic127
Description: Animation library at terminal
'''

import itertools as _iter, time as _t

def _build(full):
    """Prepairer"""
    frames = []
    for i in range(len(full)):
        frames.append(full[i:] + full[:i])
    return frames
    
def _loop(frames, delay, withRev=False):
    """Loop frames"""
    if withRev:
        frames = frames + frames[::-1]
    for frame in _iter.cycle(frames):
        print(frame, end="\r")
        _t.sleep(delay)

def scrollText(text: str, space="    ", delay=0.1):
    """Text scroling to X"""
    full = text + space
    frames = _build(full)
    _loop(frames, delay)
        
def scrollList(List: list, space="    ", delay=0.1):
    """List of texts scrolling to x"""
    full = space.join(List) + space
    frames = _build(full)
    _loop(frames, delay)
        
def pingPongText(text: str, space="    ", delay=0.1):
    """Ping-pong like text"""
    full = text + space
    frames = _build(full)
    _loop(frames, delay, withRev=True)

def mainfunc():
    scrollText("Hello, World!")
    
if __name__ == '__main__':
    mainfunc()
