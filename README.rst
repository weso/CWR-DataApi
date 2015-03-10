CWR Data Model API
===================

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

Status
------

The project is still in the development phase.

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues page`_.

Documentation
-------------

Documentation for the project can be found at the GitHub `project
wiki`_.

Building the code
-----------------

The application has been coded in Python, and tested for various
versions of the Python 2 and 3 interpreter.

Dependencies are indicated on requirements.txt.

Prerequisites
~~~~~~~~~~~~~

Requires Python, and has been tested on the following interpreters:

- Python 2 (2.6, 2.7)
- Python 3 (3.2, 3.3, 3.4)
- Pypy

The dependencies can be acquired using the list on requirements.txt,
with the command:

``pip install -r requirements.txt``

Getting the code
~~~~~~~~~~~~~~~~

The code can be found at the GitHub `project page`_.

To acquire it through Git use the following clone URI:

``git clone https://github.com/weso/CWR-DataApi.git``

Continuous integration
----------------------

The continuous integration information can be found at the `project CI
page`_ based on Travis CI.

License
-------

The project is released under the `MIT License`_.

.. _CISAC: http://www.cisac.org/
.. _BMAT: http://www.bmat.com/
.. _WESO: http://www.weso.es/
.. _project issues page: https://travis-ci.org/weso/CWR-DataApi/issues
.. _project wiki: https://github.com/weso/CWR-DataApi/wiki
.. _project page: https://github.com/weso/CWR-DataApi
.. _project CI page: https://travis-ci.org/weso/CWR-DataApi
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
