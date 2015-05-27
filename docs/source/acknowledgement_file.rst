====================
Acknowledgement file
====================

After receiving and processing the CWR file, the recipient will create and
return an acknowledgement file, containing most of the original file
information, and adding Acknowledgement Transactions.

These transactions will include all additional information that may be needed,
such as the reasons for rejecting a transaction, or the CAE/IPI numbers where
they may be missing.

Information that is not relevant to the creator of the Acknowledgment file will
not appear on it. For example, a society will generally not return SPU/SPT
records for sub-publishers in territories it does not control.

Note that when validating the original CWR file the process won't stop at the
first error encountered, but will continue to report all errors, unless a
severe error makes further processing inadvisable.

----------------------
Acknowledgement report
----------------------

According to the CWR standard, along the Acknowledgment file a form must be
fulfilled and sent back to the submitter.

This contains the transmission participants:

- Society
- Sender (of the original CWR file)

And also a series of details:

- File name
- Location
- Description
- File size
- Date or time stamp (YYYYMMDD and HHMMSS format)
- Number of transactions and records

Along a series of boolean flags:

- The file has been received and is awaiting validation/processing
- The file has been received and has been successfully validated/processed
- The file is no longer required and can be deleted
- The file has been received and has failed validation/processing (It should be sent again and details of failure are to be indicated to the sender)

---------------------------
Acknowledgement transaction
---------------------------

Information on the Acknowledgement file is added with the use of
Acknowledgement transactions.

These mark the Transactions on the original file, adding any needed information
about them, such as if it has been rejected.

It follows the structure: [ACK, MSG*, AGR | NWR | REV | EXC]