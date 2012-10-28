#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
ZabbixAPI

This software is licensed as described in the README.md file, which you should
have received as part of this distribution.
"""
import os
from setuptools import setup, find_packages, findall


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='zabbixAPI',
    url='https://github.com/ricco386/zabbixAPI',
    version='0.1',
    license='GNU LGPL 2.1',
    author='Aleksandr Balezin',
    author_email='gescheit@list.ru',
    description='Zabbix API',
    long_description=read('README.md'),
    keywords="zabbix api monitoring",
    py_modules=['zabbixAPI'],
    packages=['zabbixAPI'],
    platforms='any',
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Library or Lesser General Public \
License (LGPL)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: System :: Systems Administration",
        ]
)
