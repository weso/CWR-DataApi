=========================
Transmission Header (HDR)
=========================

The Transmission header indicates the begginning of the CWR data on the file,
and contains information about it's creation and sender.

It contains the following fields:

===========================  ============  ========  ===========
Field                        Type          Required  Description
===========================  ============  ========  ===========
Record Type                  Alphanumeric  Yes       It is always 'HDR'
Sender Type                  Alphanumeric  Yes       Indicates the role of the sender. Only 'AA', 'PB', 'SO' or 'WR' are accepted.
Sender ID                    Numeric       Yes       Code identifying the sender
Sender Name                  Alphanumeric  Yes       Name of the sender
EDI Standard Version Number  Alphanumeric  Yes       Version of the header and trailer. '01.10' for CWR 2.1
Creation Date                Date          Yes       The date that this file was created
Creation Time                Time          Yes       The time of day that this file was created
Transmission Date            Time          Yes       The date that this file was transmitted to all receiving entities
Character Set                Time          No        To be used if this file contains data in a character set other than ASCII
===========================  ============  ========  ===========