============================
Acknowledgement Record (ACK)
============================

This record indicates the transaction status after its validation, along any
information needed to link this transaction with the original one.

===========================================================  =======================================  ========  ===========
Field                                                        Type                                     Required  Description
===========================================================  =======================================  ========  ===========
Original Transaction Sequence #                              Numeric                                  Yes       The sequence number of the original transaction
Original Transaction Type                                    Table Lookup (Transaction Type Table)    Yes       The type of the original transaction
Processing Date                                              Date                                     Yes       The date the file was received
Transaction Status                                           Table Lookup (Transaction Status Table)  Yes       Current status for the Transaction
Creation Title                                               Alphanumeric                             No        If the original transaction reffers to a work, its title should be here
Submitter Creation #                                         Numeric                                  No        ID assigned by the submitter. Required if the original Transaction was accepted
Recipient Creation #                                         Numeric                                  No        ID assigned by the recipient. Required if the original Transaction was accepted
===========================================================  =======================================  ========  ===========
