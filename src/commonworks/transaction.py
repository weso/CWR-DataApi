# -*- encoding: utf-8 -*-

"""
Transaction model classes.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class AgreementTransaction(object):
    """
    Represents a CWR Agreement Transaction (AGR).
    """

    def __init__(self, agreement, territories):
        self._agreement = agreement
        self._territories = territories

    @property
    def agreement(self):
        """
        Agreement Supporting Work Registration field.

        The Agreement record in the transaction.

        :return:
        """
        return self._agreement

    @property
    def territories(self):
        """
        The territories affected by this Agreement and their IPAs.

        This is a collection if TerritoryWithIPAs.

        :return: the territories affected by this Agreement and their IPAs
        """
        return self._territories


class WorkTransaction(object):
    """
    Represents a CWR Work Transaction.

    These can be a New Work Registration (NWR), Revised Registration (REV), Notification of ISWC assign to a work (ISW)
    or Existing work which is in Conflict with a Work Registration (EXC).
    """

    def __init__(self, entire_work_title=None, original_work_title=None, recording=None, alternate_titles=None,
                 publishers_controlled=None, publishers_other=None, writers_controlled=None,
                 writers_other=None, performers=None, origins=None, inst_summaries=None,
                 inst_details=None, components=None, info=None):
        self._entire_work_title = entire_work_title
        self._original_work_title = original_work_title
        self._recording = recording
        self._info = info

        if alternate_titles is None:
            self._alternate_titles = []
        else:
            self._alternate_titles = alternate_titles

        if publishers_controlled is None:
            self._publishers_controlled = []
        else:
            self._publishers_controlled = publishers_controlled

        if publishers_other is None:
            self._publishers_other = []
        else:
            self._publishers_other = publishers_controlled

        if writers_controlled is None:
            self._writers_controlled = []
        else:
            self._writers_controlled = writers_controlled

        if writers_other is None:
            self._writers_other = []
        else:
            self._writers_other = writers_other

        if performers is None:
            self._performers = []
        else:
            self._performers = performers

        if origins is None:
            self._origins = []
        else:
            self._origins = origins

        if inst_summaries is None:
            self._inst_summaries = []
        else:
            self._inst_summaries = inst_summaries

        if inst_details is None:
            self._inst_details = []
        else:
            self._inst_details = inst_details

        if components is None:
            self._components = []
        else:
            self._components = components

    @property
    def alternate_titles(self):
        """
        Alternate Titles field.

        Returns the Alternate Titles for the Work.

        :return: the Alternate Title for the Work
        """
        return self._alternate_titles

    @property
    def components(self):
        """
        Components field.

        Returns the Work Components.

        :return: the Work Components
        """
        return self._components

    @property
    def entire_work_title(self):
        """
        Entire Work Title field.

        Returns an Entire Work Title for the Work.

        :return: an Entire Work Title for the Work
        """
        return self._entire_work_title

    @property
    def info(self):
        """
        Additional Info field.

        Contains information such as comments or the Society number.

        This is a collection of strings.

        :return: additional info for the work
        """
        return self._info

    @property
    def inst_details(self):
        """
        Instrumentation Details field.

        Returns the Work Instrumentation Details.

        :return: the Work Instrumentation Details
        """
        return self._inst_details

    @property
    def inst_summaries(self):
        """
        Instrumentation Summaries field.

        Returns the Work Instrumentation Summaries.

        :return: the Work Instrumentation Summaries
        """
        return self._inst_summaries

    @property
    def original_work_title(self):
        """
        Original Work Title field.

        Returns an Original Work Title for the Work.

        :return: an Original Work Title for the Work
        """
        return self._original_work_title

    @property
    def origins(self):
        """
        Work Origins field.

        Returns the Work Origins.

        :return: the Work Origins
        """
        return self._origins

    @property
    def performers(self):
        """
        Performing Artists field.

        The Performing Artists.

        :return: the Performing Artists
        """
        return self._performers

    @property
    def publishers_controlled(self):
        """
        Publisher Controlled by Submitter field.

        List all publishers controlled by the submitter.  This record is mandatory if writer ownership shares are less
        than 100%.

        This is a collection of PublisherWithTerritories.

        :return: the publishers controlled by the submitter
        """
        return self._publishers_controlled

    @property
    def publishers_other(self):
        """
        Other Publishers field.

        Lists all the publishers not controlled by the submitter.

        This is just a collection of Publishers.

        :return: the Publishers not controlled by the submitter
        """
        return self._publishers_other

    @property
    def recording(self):
        """
        Recording field.

        Recording status.

        :return: the Recording status
        """
        return self._recording

    @property
    def writers_controlled(self):
        """
        Writers Controlled by Submitter field.

        Lists all the Writers controlled by the submitter.

        This is a collection of WriterWithTerritoryPublishers.

        :return: all the Writers controlled by the submitter along his Territories and Publishers
        """
        return self._writers_controlled

    @property
    def writers_other(self):
        """
        Other Writers field.

        List all the Writers not controlled by the submitter.

        This is just a collection of Writers.

        :return: the Writers not controlled by the submitter
        """
        return self._writers_other


class PublisherWithTerritories(object):
    """
    Represents a Publisher and his territories.
    """

    def __init__(self, publisher, territories=None):
        self._publisher = publisher

        if territories is None:
            self._territories = []
        else:
            self._territories = territories

    @property
    def publisher(self):
        """
        The Publisher.

        Returns the Publisher which affects the territories.

        :return: the Publisher
        """
        return self._publisher

    @property
    def territories(self):
        """
        The territories.

        Returns the territories to which the Publisher affects.

        :return: the territories of the Publisher
        """
        return self._territories


class TerritoryWithIPAs(object):
    """
    Represents a Territory and its IPAs
    """

    def __init__(self, territory, ipas):
        self._territory = territory
        self._ipas = ipas

    @property
    def ipas(self):
        """
        The Interested Parties of the Agreement which affect this Territory.

        :return: the Territory IPAs
        """
        return self._ipas

    @property
    def territory(self):
        """
        The Territory.

        :return: the Territory
        """
        return self._territory


class WriterWithTerritoryPublisher(object):
    """
    Represents a Writer along his Territories and Publishers.
    """

    def __init__(self, writer, territories=None, publishers=None):
        self._writer = writer

        if territories is None:
            self._territories = []
        else:
            self._territories = territories

        if publishers is None:
            self._publishers = []
        else:
            self._publishers = publishers

    @property
    def publishers(self):
        """
        Publishers representing the Writer.

        :return: all the Publishers representing the Writer
        """
        return self._publishers

    @property
    def territories(self):
        """
        Territories of the Writer.

        :return: the Territories of the Writer
        """
        return self._territories

    @property
    def writer(self):
        """
        The Writer.

        :return: the Writer
        """
        return self._writer