#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os.path import exists


maintainer = "Eoghan N. O'Connell"
maintainer_email = "eoghan.n.oconnell@gmail.com"
description = 'Polarisation characterisation of HREM data.'
name = "topotem"
year = "2021"


setup(
    name=name,
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    url='https://github.com/TopoTEM/TopoTEM',
    version='0.0.1',
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,
    license="GPL v3",
    description=description,
    long_description=open('README.rst').read() if exists('README.rst') else '',
    install_requires=[],
    python_requires=">=3.6",
    keywords=["TEM", "STEM", "polarisation", "polarization",
              "electron microscopy", "atomic resolution"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization',
        'Intended Audience :: Science/Research',
        ],
    )
