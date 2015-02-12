# -*- encoding: utf-8 -*-

"""
CWR transaction classes.

These files are not meant to store all the data of the transaction, that is done with the other model files,
but to indicate the relationships contained in these transactions.

For example, an Agreement Transaction would indicate an Agreement, the Territories it applies to and the
Interested Parties for each Territory. While the concrete information of that Agreement, Territories and
Interested Parties are stored in their own model classes.

When representing a full CWR file these transmissions should be stored on the Transmission classes from the file
module. More precisely, they should be contained in a TransactionGroup.

A transaction is a composition of records, the first of which is called the transaction header. This is the record
giving the name for the transaction, so for example an Agreement Transaction means that the header record
is an Agreement Record.

This header will describe the Transaction.

The possible transactions in CWR v2.1 are:
- Acknowledgment of Transaction (ACK)
- Agreement supporting Work Registration (AGR)
- Existing Work which is in conflict with a Work registration (EXC)
- New Works Registration (NWR)
- Notification of ISWC assigned to a Work (ISW)
- Revised Registration (REV)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'
