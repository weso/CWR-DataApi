# -*- coding: utf-8 -*-


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
        i = 1
        for group in transmission.groups:
            print ' '
            print '------------------------------'
            print '******************************'
            print '*           GROUP            *'
            print '******************************'
            print '------------------------------'
            print ' '
            print '------------------------------'
            print 'Group %s' % (i)
            print 'Contains %s transactions' % (len(group.transactions))
            print '------------------------------'
            self.print_group_header(group.group_header)
            print '------------------------------'
            self.print_group_trailer(group.group_trailer)

            for transaction in group.transactions:
                print ' '
                print '------------------------------'
                print '******************************'
                print '*        TRANSACTION         *'
                print '******************************'
                print '------------------------------'
                print ' '
                print '------------------------------'
                self.print_transaction_record(transaction)
            i += 1

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

    def print_group_header(self, header):
        print 'CWR Group Header'
        print 'Record Type: %s' % (header.record_type)
        print 'Group ID: %s' % (header.group_id)
        print 'Transaction Type: %s' % (header.transaction_type)
        print 'Version Number: %s' % (header.version_number)
        print 'Batch Request ID: %s' % (header.batch_request_id)

    def print_group_trailer(self, header):
        print 'CWR Group Trailer'
        print 'Record Type: %s' % (header.record_type)
        print 'Group ID: %s' % (header.group_id)
        print 'Transaction Count: %s' % (header.transaction_count)
        print 'Record Count: %s' % (header.record_count)

    def print_transaction_record(self, record):
        print 'Record Type: %s' % (record.record_type)
        print 'Transaction Sequence Number: %s' % (record.transaction_sequence_n)
        print 'Record Sequence Number: %s' % (record.record_sequence_n)