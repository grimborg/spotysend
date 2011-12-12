#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

curdir = os.path.dirname(os.path.abspath(__file__))

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name = 'spotysend',
    description = 'send commands to Spotify',
    long_description = read('README.rst'),
    license = 'http://www.gnu.org/licenses/gpl-2.0.html',
    version = '1.0',
    author = 'Òscar Vilaplana',
    author_email = 'dev@oscarvilaplana.cat',
    url = 'https://github.com/grimborg/spotysend',
    install_requires = ['opster'],
    py_modules = ['spotysend'],
    entry_points = {'console_scripts': ['spotysend=spotysend:send_command.command', ]},
    )
