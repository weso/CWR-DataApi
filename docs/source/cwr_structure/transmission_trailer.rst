==========================
Transmission Trailer (TRL)
==========================

The Group Trailer closes a CWR file, and contains validation information.

This validation data is the number of groups, transactions and records which
should have been processed.

It contains the following fields:

=================  ============  ========  ===========
Field              Type          Required  Description
=================  ============  ========  ===========
Record Type        Alphanumeric  Yes       It is always 'TRL'
Group Count        Numeric       Yes       Number of transactions in the Transmission
Transaction Count  Numeric       Yes       Number of transactions in the Transmission
Record Count       Numeric       Yes       Number of records in the Transmission
=================  ============  ========  ===========