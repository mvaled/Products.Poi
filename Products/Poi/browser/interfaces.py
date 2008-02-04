from zope.interface import Interface


class IIssueFolderView(Interface):
    """Abstract a PoiTracker into a folder for issues.
    """

    def getFilteredIssues(criteria, **kwargs):
        """Get the contained issues in the given criteria.
        """

    def getIssueSearchQueryString(criteria, **kwargs):
        """Return a query string for an issue query.
        """

    def buildIssueSearchQuery(criteria, **kwargs):
        """Build canonical query for issue search.
        """

    def getMyIssues(openStates, memberId, manager):
        """Get a catalog query result set of my issues.

        So: all issues assigned to or submitted by the current user,
        with review state in openStates.

        If manager is True, you can add more states.
        """

    def getOrphanedIssues(openStates, memberId):
        """Get a catalog query result set of orphaned issues.

        Meaning: all open issues not assigned to anyone and not owned
        by the given user.
        """


import zope.schema
from zope.interface import directlyProvides
from zope.viewlet.interfaces import IViewletManager
from zope.contentprovider.interfaces import ITALNamespaceData


class IResponseAdder(IViewletManager):

    def getAvailableIssueTransitions():
        """Get the available transitions for this issue.
        """

    def getAvailableSeverities():
        """Get the available severities for this issue.
        """

    def getReleasesVocab():
        """Get the releases from the project.
        """

    def getManagersVocab():
        """Get the tracker managers.
        """

directlyProvides(IResponseAdder, ITALNamespaceData)


class ICreateResponse(Interface):
    pass

