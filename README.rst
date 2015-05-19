CWR Data Model API
==================

This projects offers a domain model for the CISAC CWR standard v2.1 to be
used on Python applications.

CWR stands for Common Works Registration, and it is a common or standard
format for the registration and revision of musical works, used by
publishers and performing rights societies as a way to exchange musical
works data.

While the CWR standard has been created by `CISAC`_ this library has been
developed by `WESO`_ independently, with help from `BMAT`_.

The library includes a data model for representing the contents of a CWR
file, and parsers to create that model from a file, and to decode and
encode JSON messages with the data model.

Documentation
-------------

The current version is under development. No public documentation is still offered.

Status
------

The project is still in the development phase.

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues page`_.

Building the code
-----------------

The application has been coded in Python, without using any particular framework.

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

Al other dependencies are indicated on requirements.txt. The included makefile can install them with the command:

``make requirements``

Getting the code
~~~~~~~~~~~~~~~~

The code can be found at the `GitHub project page`_.

License
-------

The project has been released under the `MIT License`_.

.. _CISAC: http://www.cisac.org/
.. _BMAT: http://www.bmat.com/
.. _WESO: http://www.weso.es/
.. _project issues page: https://github.com/weso/CWR-DataApi/issues
.. _GitHub project page: https://github.com/weso/CWR-DataApi
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
