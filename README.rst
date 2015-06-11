CWR Data Model API
==================

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/weso/CWR-DataApi
   :target: https://gitter.im/weso/CWR-DataApi?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

This projects offers a domain model for the CISAC CWR standard v2.1 to be
used on Python applications, along a series of parsing which allow
transformations between the model and various data structures.

CWR stands for Common Works Registration, and it is a common or standard
format for the registration and revision of musical works, used by
publishers and performing rights societies as a way to exchange musical
works data.

While the CWR standard has been created by `CISAC`_ this library has been
developed by `WESO`_ independently, with help from `BMAT`_.

Features
--------

- Model for CWR files
- Configurable parser from transforming a CWR file into the model classes (including Pyparsing grammar)
- Parsers for for model-JSON transformations

Documentation
-------------

Check the `latest docs`_ for the most current version of the documentation.

They are generated with the help of `Sphinx`_. The source files for this are
stored in the docs folder.

Building the code
-----------------

The application has been coded in Python, without using any particular
framework.

Prerequisites
~~~~~~~~~~~~~

The project has been tested in the following versions of the interpreter:

- Python 2.6
- Python 2.7
- Python 3.2
- Python 3.3
- Python 3.4
- Pypy
- Pypy 3

All other dependencies are indicated on the requirements.txt file.
The included makefile can install them with the command:

``make requirements``

Among them, the most important is the `Pyparsing`_ library, which is used
to create the CWR file parser.

Installing
~~~~~~~~~~

The project includes a setup.py file and a makefile allowing direct
installation of the library.

This can be done with the following command:

``make install``

Additionally, the project is offered as a `Pypi package`_, and can be installed through pip:

``pip install cwr-api``

Collaborate
-----------

The project is still under ongoing development, and any help will be well
received.

There are two ways to help: reporting errors and asking for extensions through
the issues management, or forking the repository and extending the project.

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues page`_.

Everybody is allowed to report bugs or ask for features.

Getting the code
~~~~~~~~~~~~~~~~

The code can be found at the `GitHub project page`_.

Feel free to fork it, and share the changes.

License
-------

The project has been released under the `MIT License`_.

.. _CISAC: http://www.cisac.org/
.. _BMAT: http://www.bmat.com/
.. _WESO: http://www.weso.es/
.. _project issues page: https://github.com/weso/CWR-DataApi/issues
.. _Pyparsing: https://pyparsing.wikispaces.com/
.. _Pypi package: https://pypi.python.org/pypi/CWR-API
.. _Sphinx: http://sphinx-doc.org/
.. _latest docs: http://cwr-dataapi.readthedocs.org
.. _GitHub project page: https://github.com/weso/CWR-DataApi
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
