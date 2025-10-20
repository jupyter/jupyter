#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function

import os
from setuptools import setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))

with open(pjoin(here, "long_description.md")) as f:
    long_description = f.read()

setup_args = dict(
    name                = 'jupyter',
    version             = '1.2.0.dev0',
    description         = "Jupyter metapackage. Install all the Jupyter components in one go.",
    long_description    = long_description,
    long_description_content_type = "text/markdown",
    author              = "Jupyter Development Team",
    author_email        = "jupyter@googlegroups.org",
    py_modules          = [],
    install_requires    = [
        'notebook',
        'nbconvert',
        'ipykernel',
        'ipywidgets',
        'jupyterlab',
    ],
    url                 = "https://jupyter.org",
    license             = "BSD",
    python_requires     = '>=3.6',
    classifiers         = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)

setup(**setup_args)
