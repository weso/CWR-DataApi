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
    xx - Version of the CWR standard

    So according to this, the files sent between a sender and a receiver each year are numerated following a sequence.
    Then a termination is added indicating the version of the CWR standard specification used on the file.
    """

    def __init__(self, year, sequence_n, sender, receiver, version):
        self._year = year
        self._sequence_n = sequence_n
        self._sender = sender
        self._receiver = receiver
        self._version = version

    @property
    def year(self):
        """
        The year in which the file has been created.

        :return: the file's year
        """
        return self._year

    @property
    def sequence_n(self):
        """
        File sequence number.

        This is nth file sent from the sender to the receiver. So if the sequence number is 10 this would be the tenth
        file sent.

        :return: the file sequence number
        """
        return self._sequence_n

    @property
    def sender(self):
        """
        The file sender.

        This is stored as an alphanumeric code.

        :return: the file sender alphanumeric code
        """
        return self._sender

    @property
    def receiver(self):
        """
        The file receiver.

        This is stored as an alphanumeric code.

        :return: the file receiver alphanumeric code
        """
        return self._receiver

    @property
    def version(self):
        """
        The CWR standard specification used to code the file.

        :return: the CWR standard specification used
        """
        return self._version


