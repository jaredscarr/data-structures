# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='data-structures',
    description="Various data-structure assignments",
    version=0.1,
    author="Daniel Swelling and Jared Scarr",
    author_email="jaredscarr@gmail.com",
    license='MIT',
    py_modules=['mail_room'],
    # package_dir={'': 'mail-room'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
)
