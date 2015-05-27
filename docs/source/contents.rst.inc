----------------
The CWR standard
----------------

The CWR file standard has been created by {{{www.cisac.org}CISAC}} as a way
for publishers and societies to share discographic information.

CWR files containing updated information are created, sent by a sending party
to a receiver, and then processed before an acknowledgement file is returned.

.. toctree::
   :maxdepth: 2

   documents
   cwr_file_structure
   cwr_field_format
   cwr_file_validation
   acknowledgement_file
   cwr_miscellany
   cwr_glossary

---------------------------------------
Other standards and related information
---------------------------------------

The CWR standard makes use of other standards or sources of data, which are
documented on this section.

.. toctree::
   :maxdepth: 2

   ipi_number

--------------------------------
The CWR file structure in detail
--------------------------------

This section contains a more detailed view of how is data stored inside a CWR
file.

.. toctree::
   :maxdepth: 2

   record_type_codes
   record_prefix
   transmission_header
   transmission_trailer
   group_header
   group_trailer
   acknowledgement_record
   message_record

-------------------
CWR file validation
-------------------

This section contains a more detailed view of how is a CWR file validated.

.. toctree::
   :maxdepth: 2

   validation_process
   file_validation
   record_prefix_validation

-------------
The model API
-------------

Being as it is the backbone of the library, the CWR file model API should be
presented first.

.. toctree::
   :maxdepth: 2

   acknowledgement_module