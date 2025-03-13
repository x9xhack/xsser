#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:
"""
This file is part of the XSSer project, https://xsser.03c8.net

Copyright (c) 2010/2021 | psy <epsylon@riseup.net>

xsser is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software Foundation version 3 of the License.

xsser is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along
with xsser; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

from setuptools import setup, find_packages

setup(
    name="xsser",
    version="1.8.4",
    packages=find_packages(include=['core', 'core.*']),
    package_data={
        "core.fuzzing": ["fuzzing/*.txt"],  # Ensures user-agents.txt is included
        "gtk": ["images/*", "docs/*", "xsser.ui", "xsser.desktop"],
    },
    include_package_data=True,
    scripts=["xsser"],
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "beautifulsoup4",
        "cairocffi",
        "gobject",
        "pycurl",
        "pygeoip",
        "selenium"
    ],
)
