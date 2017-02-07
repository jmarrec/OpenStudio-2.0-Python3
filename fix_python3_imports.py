#!/usr/bin/python3

"""
Run this script exactly once in your ./openstudio/ folder where you have placed
all the .py and .so files already.

"""

import glob as gb
import fileinput
import re

re_import = re.compile(r'^import (openstudio.*?)( as .*)?$')
re_from = re.compile(r'^from (openstudio.*?) import (.*)?$')

pyfiles = [f for f in gb.glob("openstudio/*.py") if not f.startswith('__')]

for line in fileinput.input(pyfiles, inplace=True, backup='.bak'):
    if 'import' in line:
        if re_import.match(line):
            line = re_import.sub(r'from .import \1\2', line)
        elif re_from.match(line):
            line = re_from.sub(r'from .\1 import \2', line)
    print(line)
