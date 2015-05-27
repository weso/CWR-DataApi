================
CWR field format
================

CWR records are divided into fields, each following a clear pattern, which
consists on defining the following properties:

- Field name
- Start index
- Size
- Format

The field name is used only to help humans identifying the field, while the
start index and size serve to acquire the data from the record line.

-------
Formats
-------

=================  ====  =====
Format             Code  Notes
=================  ====  =====
Alphanumeric       A     ASCII characters in upper case.
Boolean            B     A single character. Can be 'Y', for yes, or 'N', for no. Meaning the Boolean values True and False.
Flag               F     The same as Boolean, but adding a third option: 'U' for unknown. This can't be parsed into a Boolean value.
Date               D     Eight numeric characters, following the pattern YYYYMMDD.
Numeric            N     Usually an integer, sometimes a float value. In that case the field documentation indicates how many characters are for the decimal value.
Time               T     Six numeric characters, following the pattern HHMMSS. It is on military format (24 hours, and not two groups of 12).
List/Table Lookup  L     Only accepts values coming from a specific list or table. The table is indicated in the field description.
=================  ====  =====

------------
Empty fields
------------

Fields may be optional, or there may not be any data to put in them. In those
cases, the empty columns must be filled as follows.

=================  ====  ==========
Format             Code  When empty
=================  ====  ==========
Alphanumeric       A     Columns should be filled with the empty character.
Boolean            B     ?
Flag               F     Should be set as 'unknown' ('U').
Date               D     Columns should be set as 0.
Numeric            N     Columns should be set as 0.
Time               T     Columns should be set as 0.
List/Table Lookup  L     Columns should be filled with the empty character.
=================  ====  ==========

----------------------
Additional constraints
----------------------

Date and Time formats have additional constraints due to the patterns they follow.

Date follows the pattern YYYYMMDD, which has the following constraints:

- YYYY: can be any number
- MM: ranges from 01 to 12
- DD: ranges from 01 to 31

Time follows the pattern HHMMSS, which has the following constraints:

- HH: ranges from 00 to 23
- MM: ranges from 00 to 59
- SS: ranges from 00 to 59