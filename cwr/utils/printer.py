# -*- encoding: utf-8 -*-


"""
This is a small tool to print a CWR file contents on the console.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class CWRPrinter():
    """
    Prints the contents of a CWR file on the console.
    """

    def __init__(self):
        pass

    def print_transmission(self, transmission):
        print transmission
        print 'CWR Transmission begins'
        print 'Contains %s groups' % (len(transmission.groups))
        print '------------------------------'
        self.print_transmission_header(transmission.header)
        print '------------------------------'
        self.print_transmission_trailer(transmission.trailer)

    def print_transmission_header(self, header):
        print 'CWR Transmission Header'
        print 'Record Type: %s' % (header.record_type)
        print 'Sender ID: %s' % (header.sender_id)
        print 'Sender Name: %s' % (header.sender_name)
        print 'Sender Type: %s' % (header.sender_type)
        print 'Created on: %s' % (header.creation_date_time)
        print 'Sent on: %s' % (header.transmission_date)
        print 'EDI standard: %s' % (header.edi_standard)
        print 'Character set: %s' % (header.character_set)

    def print_transmission_trailer(self, header):
        print 'CWR Transmission Trailer'
        print 'Record Type: %s' % (header.record_type)
        print 'Group Count: %s' % (header.group_count)
        print 'Transaction Count: %s' % (header.transaction_count)
        print 'Record Count: %s' % (header.record_count)