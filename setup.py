# -*- encoding: utf-8 -*-
from distutils.core import setup

"""
PyPI configuration module.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'

setup(
    name='cwr_api',
    packages=['cwr', 'cwr.utils'],
    version='0.1',
    description='API library for the CWR standard format',
    author='WESO',
    author_email='',
    url='https://github.com/weso/CWR-DataApi',
    download_url='https://github.com/weso/CWR-DataApi',
    keywords=['CWR', 'cwr', 'api'],
    classifiers=[],
    license='MIT',
    long_description=open("README.rst").read(),
)