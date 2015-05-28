========================
Record Prefix validation
========================

----------------------
Field level validation
----------------------

=========  ======================  =============================================================  =============
ID         Field                   Constraint                                                     Failure level
=========  ======================  =============================================================  =============
1          Record Type             Should be one from the Record Type or Transaction Type tables  ER
2,3,4,7,8  Transaction Sequence #  See below                                                      TR/ER
5,6        Record Sequence #       See below                                                      ER
=========  ======================  =============================================================  =============

------------------------------
Transaction sequence numbering
------------------------------

- For the first Transaction header of a group it should be 0 (id 2, fl ER)
- For Transaction headers not being the first in the group, this is equal to the previous transaction number plus one (id 3, fl TR)
- For detail records the code is the same as the last transaction header (id 4, fl TR)
- Transactions sequence numbers should be sequential (id 7, fl ER)
- Detail records on a Transaction should have this Transaction's sequence number (id 8, fl ER)

-------------------------
Record sequence numbering
-------------------------

- For Transaction headers it should be 0 (id 5, fl ER)
- For details records this is equal to the previous record number plus one (id 6, fl ER)