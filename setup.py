# -*- coding: utf-8 -*-
import ast
import re
from codecs import open
from os import path

from setuptools import setup, find_packages


"""
PyPI configuration module.

This is prepared for easing the generation of deployment files.
"""

__license__ = 'MIT'
__version__ = '1.0.0'

# Regular expression for the version
_version_re = re.compile(r'__version__\s+=\s+(.*)')

# Test requirements
_tests_require = []

# Path to the project's root
here = path.abspath(path.dirname(__file__))

# Gets the long description from the readme
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Gets the version for the source folder __init__.py file
with open('cwr/__init__.py', 'rb', encoding='utf-8') as f:
    version = f.read()
    version = _version_re.search(version).group(1)
    version = str(ast.literal_eval(version.rstrip()))

setup(
    name='CWR-API',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'data_commonworks': ['data_commonworks/*.csv', 'data_commonworks/*.yml'],
        'config_commonworks': ['config_commonworks/*.yml'],
    },
    version=version,
    description='API library for the CWR standard format',
    author='WESO',
    author_email='weso@weso.es',
    license='MIT',
    url='https://github.com/weso/CWR-DataApi',
    download_url='https://pypi.python.org/pypi/CWR-API',
    keywords=['CWR', 'commonworks', 'api', 'CISAC', 'parser'],
    platforms='any',
    classifiers=['License :: OSI Approved :: MIT License', 'Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers', 'Operating System :: OS Independent',
                 'Programming Language :: Python', 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.6', 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3', 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: Implementation :: PyPy',
                 'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description=long_description,
    install_requires=[
        'chardet',
        'pyparsing',
        'pyyaml',
        'setuptools',
    ],
    tests_require=_tests_require,
    extras_require={'test': _tests_require},
)