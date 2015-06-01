===================
Group Trailer (GRT)
===================

The Group Trailer closes a batch of transactions, and contains validation
information.

This validation data is the number of transactions and records which should
have been processed.

It contains the following fields:

=================  ============  ========  ===========
Field              Type          Required  Description
=================  ============  ========  ===========
Record Type        Alphanumeric  Yes       It is always 'GRT'
Group ID           Numeric       Yes       The same as the header
Transaction Count  Numeric       Yes       Number of transactions in the group
Record Count       Numeric       Yes       Number of records in the group
=================  ============  ========  ===========