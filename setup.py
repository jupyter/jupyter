#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Juptyer Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function

import os
import sys

from distutils.core import setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))


setup_args = dict(
    name                = 'jupyter',
    version             = '1.0.0',
    description         = "Jupyter metapackage. Install all the Jupyter components in one go.",
    long_description    = """Install the Jupyter system, including the notebook, qtconsole, and the IPython kernel.""",
    author              = "Jupyter Development Team",
    author_email        = "jupyter@googlegroups.org",
    py_modules          = ['jupyter'],
    install_requires    = [
        'notebook',
        'qtconsole',
        'jupyter-console',
        'nbconvert',
        'ipykernel',
        'ipywidgets',
    ],
    url                 = "http://jupyter.org",
    license             = "BSD",
    classifiers         = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)

if any(bdist in sys.argv for bdist in ['bdist_wheel', 'bdist_egg']):
    import setuptools


if __name__ == '__main__':
    setup(**setup_args)
