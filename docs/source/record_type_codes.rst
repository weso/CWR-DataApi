=================
Record Type Codes
=================

The valid Record types are always indicated in the latest CWR standard
specification, and indicated on CISAC's Record Type table.

These are used on a Record prefix to identify it's type.

This list is offered just to make it easier identifying each of them.

---------------
Control Records
---------------

===========  ===========
Record Type  Record name
===========  ===========
GRH          Group Header
GRT          Group Trailer
HDR          Transmission Header
TRL          Transmission Trailer
===========  ===========

-------------------
Transaction Records
-------------------

Note that the Transaction type is actually the type of the header Record on
the Transaction.

So for example an Acknowledgment Transaction starts with an Acknowledgment
Record.

===========  ===========
Record Type  Record name
===========  ===========
ACK          Acknowledgment of Transaction
AGR          Agreement supporting Work Registration
EXC          Existing Work which is in conflict with a Work registration
NWR          New Works Registration
ISW          Notification of ISWC assigned to a Work
REV          Revised Registration
===========  ===========

--------------
Detail Records
--------------

===========  ===========
Record Type  Record name
===========  ===========
ALT          Alternate Title
ARI          Additional Related Information
COM          Composite Component
EWT          Entire Work Title for Excerpts
IPA          Interested Party of Agreement
IND          Instrumentation Detail
INS          Instrumentation Summary
MSG          Message
NAT          Non-Roman Alphabet Title
NCT          Non-Roman Alphabet Title for Components
NET          Non-Roman Alphabet Entire Work Title for Excerpts
NOW          Non-Roman Alphabet Other Writer Name
NPN          Non-Roman Alphabet Publisher Name
NPR          Performing Artist in Non-Roman alphabet
NVT          Non-Roman Alphabet Original Title for Versions
NWN          Non-Roman Alphabet Writer Name
OPU          Other Publisher
ORN          Work Origin
OWR          Other Writer
PER          Performing Artist
PWR          Publisher for Writer
REC          Recording Detail
SPT          Publisher Territory of Control
SPU          Publisher Controlled by Submitter
SWR          Writer Controlled by Submitter
SWT          Writer Territory of Control
TER          Territory in Agreement
VER          Original Work Title for Versions
===========  ===========