==================
Group Header (GRH)
==================

The Group header indicates the begginning of a batch CWR transactions on the
file.

It contains the following fields:

================  =====================================  ========  ===========
Field             Type                                   Required  Description
================  =====================================  ========  ===========
Record Type       Alphanumeric                           Yes       It is always 'GRH'
Transaction Type  Table Lookup (Transaction Type table)  Yes       All the transactions in the group are of this type
Group ID          Numeric                                Yes       Sequential ID starting on 1
Version Number    Alphanumeric                           Yes       CWR version of the transaction. By default it is '02.10' for CWR 2.1
Batch request     Numeric                                No        ID used by the submitter to internally identify this batch
================  =====================================  ========  ===========