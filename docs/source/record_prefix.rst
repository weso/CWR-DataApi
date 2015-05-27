=============
Record Prefix
=============

All the records contain an initial field serving the uniquely identify them,
and to note the type of record it is.

------------------------------
Prefix according to the record
------------------------------

It should be noted that the prefix structure on this page applies only to
Transaction and Detail records. Control records lack the Transaction Sequence
Number and the Record Sequence Number.

-----------------------
Structure of the prefix
-----------------------

This field is the record prefix, which contains just three values:

======================  ==============  ===========
Field                   Type            Description
======================  ==============  ===========
Record Type             Table Lookup    One from the Record Type or Transaction Type tables
Transaction Sequence #  Numeric         Unique ID for each Transaction in a Group
Record Sequence #       Numeric         Unique ID for each Detail Record in a transaction
======================  ==============  ===========

Transactions and Detail Records share both sequence numbers, but use them in a
different way.

Transactions have the Record Sequence Number set to 0 always. Their Transaction
Sequence Number is 0 for the first Transaction on a Group, and a consecutive
value for the following Transactions on the same Group.

Detail Records use the Transaction Sequence Number of the Transaction they are
part of, while the Record Sequence Number is that of the previous Record plus
one.

::

    Ambiguity: the specification file is not very clear about the Detail
    Records numbering. I suppose the first Detail Record on a Transaction
    should have RSN 1 (RSN of the Transaction, which is 0, plus 1)

------------------------------
Example for sequence numbering
------------------------------

This would be an example of sequence numbering:

============================  ========================  =================
Record Type                   Transaction Sequence #	Record Sequence #
============================  ========================  =================
First transaction header      0                         0
First detail in transaction   0                         1
Second detail in transaction  0                         2
Third detail in transaction   0                         3
Second transaction header     1                         0
First detail in transaction   1                         1
Second detail in transaction  1                         2
Third transaction header      2                         0
First detail in transaction   2                         1
Second detail in transaction  2                         2
Third detail in transaction   2                         3
Fourth detail in transaction  2                         4
============================  ========================  =================