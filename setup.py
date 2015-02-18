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
    packages=['cwr', 'cwr.utils', 'cwr.parsing', 'cwr.parsing.data'],
    version='0.7',
    description='API library for the CWR standard format',
    author='WESO',
    license='MIT',
    url='https://github.com/weso/CWR-DataApi',
    download_url='https://github.com/weso/CWR-DataApi',
    keywords=['CWR', 'commonworks', 'api'],
    classifiers=['License :: OSI Approved :: MIT License', 'Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python :: 2.6', 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.2', 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4'],
    long_description=open("README.rst").read(),
)