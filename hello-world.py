#!/usr/bin/env python3

from os import getenv

name = getenv('NAME')

if name is None:
    name = 'World!'

print(f"Hello {name}")
