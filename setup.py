# -*- encoding: utf-8 -*-
import ast
import re

from setuptools import setup, find_packages


"""
PyPI configuration module.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('cwr/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='CWR-API',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='API library for the CWR standard format',
    author='WESO',
    author_email='',
    license='MIT',
    url='https://github.com/weso/CWR-DataApi',
    download_url='https://github.com/weso/CWR-DataApi',
    keywords=['CWR', 'commonworks', 'api'],
    platforms='any',
    classifiers=['License :: OSI Approved :: MIT License', 'Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers', 'Operating System :: OS Independent',
                 'Programming Language :: Python', 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.6', 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3', 'Programming Language :: Python :: 3.4'],
    long_description=open("README.rst").read(),
    install_requires=[
        'pyparsing',
        'pyyaml',
    ],
)