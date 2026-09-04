#!/usr/bin/env python3
# Made by @Ericwasepic127

from os import chdir as create_dir, remove as _rf
from shutil import rmtree as _sd
from os.path import isfile as check_file, exists as check_there
from platform import system as t

platform = t().lower()
del t

DIRECTORY_DELETE = "directory delete"
FILE_DELETE = "file delete"

def remove(path, safe=True):
    """Removes safely"""
    assert path, "Path doesn't specified"
    if safe and not check_there(path):
        raise FileNotFoundError(f"Path {path} does not exists")
    if safe is DIRECTORY_DELETE:
        _sd(path)
    if safe is FILE_DELETE:
        _sf(path)
    if check_file(path) and safe:
        _sf(path)
    elif safe and exists(path):
        _sd(path)
    else safe:
        _sf(path)
