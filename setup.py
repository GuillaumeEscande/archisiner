#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
INSTALL_REQUIRES = (HERE / "requirements.txt").read_text().splitlines()
TESTS_REQUIRE = (HERE / "test-requirements.txt").read_text().splitlines()[1:]

NAME = "archisiner"
VERSION = "0.1.0"

setup(
    name=NAME,
    version=VERSION,
    description="archisiner",
    author="Escande Guillaume",
    author_email="escande.guillaume@gmail.com",
    url="https://github.com/GuillaumeEscande/archisiner",
    keywords=["architecture", "design"],
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    packages=find_packages(),
    package_data={},
    include_package_data=True,
    entry_points={
    }
)
