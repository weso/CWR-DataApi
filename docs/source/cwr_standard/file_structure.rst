==================
CWR file structure
==================

CWR files are meant to be used as an information transmission system and
reflect this on their structure.

The information is divided in two parts: the file name contains data uniquely
identifying the file, and the contents of the file contain the actual
information being sent.

---------
File name
---------

The CWR standard gives a special importance to the file's name, certain
metadata is stored on it to allow it being used as an unique identifier for
the file.

The filename follows the pattern CWyynnnnsss_rrr.Vxx where each section means
the following:

- CW: Header indicating it is a CWR file.
- yy: Year.
- nnnn: Sequence.
- sss: Sender. 2 or 3 digits.
- rrr: Receiver. 2 or 3 digits.
- xx: Version of the CWR standard (version x.x).

::

    On the original CWR v2.1 specification the sequence number consists of only
    two digits. Was changed to four on revision 5.

Note that the filename specification is not always followed, and so by default
it should be considered optional.

--------------
File structure
--------------

The file is structured as a batch process, storing a consecutive series of
transactions.

All these transactions are grouped into a single Transmission, which is then
divided into several Groups, one for each type of transaction.

The start and ending of both the Transmission and the Groups are marked by a
header and trailer record.

So the structure of file's interior can be defined as: [HDR, [GRH, GRT]*, TRL]

Where the tags are the CWR record header tags, meaning:

- HDR: Transmission header
- TRL: Transmission trailer
- GRH: Group header
- GRT: Group trailer

These four types of record are the Control Records of the file, used not only
to separate the sections, but also to verify the data contained in them is
correct.

This is done comparing the information these records contain with the
information read from the section they enclose.

Transmission
------------

There is only single Transmission in the file, and it contains all the records.

Groups
------

Groups contain batchs of transactions.

While there are several groups on the file, there can be only one for each type
of transaction, and they indicate which type of transaction they are storing.

They are numbered consecutively, starting on 1. No two Groups may have the same
number, and there can't be any gaps between their numbers.

Transaction
-----------

A Transaction is a batch of records containing all the data for a single job.

For example, a Transaction may contain information for registering an
Agreement, for indicating a registering conflict with a Work, or even for
indicating an error on a Transaction.

A Transaction is always of a single type, which is specified by it's header
record, and will be named after it. So if a Transaction starts with an
Agreement record it is an Agreement Transaction.

The possible transactions in CWR v2.1 are:

- Acknowledgment of Transaction (ACK)
- Agreement supporting Work Registration (AGR)
- Existing Work which is in conflict with a Work registration (EXC)
- New Works Registration (NWR)
- Notification of ISWC assigned to a Work (ISW)
- Revised Registration (REV)

In practise, a Transaction is just a relationship of Records, and it indicates
which records can or should follow the header.

Going back to the previous example, an Agreement Transaction would indicate an
Agreement, the Territories it applies to and the Interested Parties for each
Territory.