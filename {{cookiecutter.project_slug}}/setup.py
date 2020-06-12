#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import setuptools

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []
setup_requirements = []
test_requirements = ["pytest"]
extra_requirements = {}

setuptools.setup(
    name="{{ cookiecutter.project_slug }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.project_short_description }}",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    version="0.1.1",
    install_requires=requirements,
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    extras_require=extra_requirements,
)
