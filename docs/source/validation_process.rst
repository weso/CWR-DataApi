==================
Validation process
==================

Once received, the file undergoes a validation process.

Three levels of validation are applied:

- Transaction level
- Record level
- Field level

The Transaction validation ensures the overall relationship between the
records is correct. This checks mainly the order, numbering and counts of
records.

Record validation checks a concrete relationship between records. For example,
a TER agreement should follow an AGR or TER agreement.

Field level validation ensures each field contains the correct information.
This checks things such as the size of the field, the pattern it must follow,
or that the references IDs exist somewhere.

--------------
Failure levels
--------------

Each validation constraint has a failure level assigned.

====  ============
Code  Failure name
====  ============
ER    Entire file is rejected
GR    Entire group is rejected
TR    Entire transaction is rejected
RR    Entire record is rejected
FR    Record is rejected and set to the default value
====  ============