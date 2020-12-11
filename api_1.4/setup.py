#!/usr/bin/env python3

from setuptools import setup, find_packages
from containerd import __api_version__, __generation__
import os

with open(os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'README.md'
          )) as f:
    ldesc = f.read()

setup(
    name='containerd',
    version='%s.%d' % (__api_version__, __generation__) ,
    description='containerd API for Python',
    long_description=ldesc,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Clustering',
        'Topic :: Utilities'
    ],
    license='Apache-2.0',
    author='Silvano Cirujano Cuesta',
    author_email='silvano.cirujano-cuesta@siemens.com',
    url='https://github.com/siemens/pycontainerd',
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'grpcio',
        'protobuf>=3.13.0'
    ]
)
