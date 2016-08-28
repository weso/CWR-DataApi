CWR Data Model API
==================

This projects offers a domain model for the CISAC CWR standard v2.1 to be
used on Python applications, along a series of parsing which allow
transformations between the model and various data structures.

CWR stands for Common Works Registration, and it is a common or standard
format for the registration and revision of musical works, used by
publishers and performing rights societies as a way to exchange musical
works data.

While the CWR standard has been created by `CISAC`_ this library has been
developed by `WESO`_ independently, with help from `BMAT`_.

.. image:: https://badge.fury.io/py/cwr-api.svg
    :target: https://pypi.python.org/pypi/cwr-api
    :alt: CWR-API Pypi package page

.. image:: https://readthedocs.org/projects/cwr-dataapi/badge/?version=latest
    :target: http://cwr-dataapi.readthedocs.org/en/latest/
    :alt: CWR-API latest documentation Status

.. image:: https://badges.gitter.im/Join%20Chat.svg
    :target: https://gitter.im/weso/CWR-DataApi?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
    :alt: Join the chat at https://gitter.im/weso/CWR-DataApi

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

Usage
-----

The application has been coded in Python. Dependencies are taken care with the
use of pip, and an included makefile helps building the project.

Prerequisites
~~~~~~~~~~~~~

The project has been tested in the following versions of the interpreter:

- Python 2.6
- Python 2.7
- Python 3.3
- Python 3.4
- Python 3.5
- Pypy
- Pypy 3

All other dependencies are indicated on the requirements.txt file.
The included makefile can install them with the command:

``$ make requirements``

Among them, the most important is the `Pyparsing`_ library, which is used
to create the CWR file parser.

Installing
~~~~~~~~~~

The project includes a setup.py file and a makefile allowing direct
installation of the library.

This can be done with the following command:

``$ make install``

Additionally, the project is offered as a `Pypi package`_, and can be installed through pip:

``$ pip install cwr-api``

Making use of the parser
~~~~~~~~~~~~~~~~~~~~~~~~

Once the project is installed it can be used in a similar way to this (using Python 2.7):

    import codecs
    import os

    from cwr.parser.decoder.file import default_file_decoder
    from cwr.parser.encoder.cwrjson import JSONEncoder

    if __name__ == '__main__':
        print('File to JSON test')
        path = raw_input(
            'Please enter the full path to a CWR file (e.g. c:/documents/file.cwr): ')
        output = raw_input(
            'Please enter the full path to the file where the results will be stored: ')
        print('\n')
        print('Reading file %s' % path)
        print('Storing output on %s' % output)
        print('\n')

        decoder = default_file_decoder()

        data = {}
        data['filename'] = os.path.basename(path)
        data['contents'] = codecs.open(path, 'r', 'latin-1').read()

        data = decoder.decode(data)

        encoder = JSONEncoder()
        result = encoder.encode(data)

        output = codecs.open(output, 'w', 'latin-1')

        output.write(result)

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
