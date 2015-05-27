====================
Message Record (MSG)
====================

Indicates the results of validation and accompanies Acknowledgement records.

==========================  ============  ========  ===========
Field                       Type          Required  Description
==========================  ============  ========  ===========
Record Prefix               Alphanumeric  Yes       The type is always 'MSG'
Message Type                List Lookup   Yes       One of 'F'/'R'/'T'/'G'/'E'
Original Record Sequence #  Numeric       Yes       The Record Sequence Number which caused this message
Record Type                 Alphanumeric  Yes       The Record Type which caused this message
Message Level               List Lookup   Yes       One of 'E'/'G'/'T'/'R'/'F'
Validation Number           Alphanumeric  Yes       Identifies the specific edit condition that generated this message
Message Text                Alphanumeric  Yes       The text associated with this message
==========================  ============  ========  ===========
