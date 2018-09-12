#!/usr/bin/env python3
from setuptools import find_packages
from setuptools import setup

import hbts

setup(
    name='hbts',
    version=hbts.__version__,
    packages=find_packages()
)

# pylint: skip-file
