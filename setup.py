# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='data-structures',
    description="Various data-structure assignments",
    version=0.1,
    author="Daniel Zwelling and Jared Scarr",
    author_email="dzwellingmusic@gmail.com, jaredscarr@gmail.com",
    license='MIT',
    py_modules=['binheap'],
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']}
)
