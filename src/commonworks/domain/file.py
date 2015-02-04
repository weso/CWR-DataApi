# -*- encoding: utf-8 -*-

"""
CWR file information model.
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class FileIdentifier(object):
    """
    Represents a CWR file identification data.

    This data identifies a concrete file and, according to the standard, is indicated in the file name, using the
    pattern CWyynnnnsss_rrr.Vxx,, where each section means the following:
    CW - Header indicating it is a CWR file.
    yy - Year.
    nnnn - Sequence. This was originally 2 numbers, later changed to 4.
    sss - Sender. 2 or 3 digits.
    rrr - Receiver. 2 or 3 digits.
    xx - Version

    So according to this, the files sent between a sender and a receiver each year are numerated following a sequence,
    and different versions of them can exist.
    """

    def __init__(self, year, sequence_n, sender, receiver, version):
        self._year = year
        self._sequence_n = sequence_n
        self._sender = sender
        self._receiver = receiver
        self._version = version


    @property
    def year(self):
        return self._year

    @property
    def sequence_n(self):
        return self._sequence_n

    @property
    def sender(self):
        return self._sender

    @property
    def receiver(self):
        return self._receiver

    @property
    def version(self):
        return self._version


