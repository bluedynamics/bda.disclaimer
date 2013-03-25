# -*- coding: utf-8 -*-

from zope.interface import implements

from Products.CMFPlone.utils import getToolByName
from Products.ATContentTypes.interface.document import IATDocument

from interfaces import IDisclaimerText

__author__ = """Robert Niederreiter <rnix@squarewave.at>"""
__docformat__ = 'plaintext'

class DisclaimerText(object):
    """Default diclaimer text implementation.
    
    Expect a ATDocument inside Plone Site root with ID ``disclaimer`` and return
    it's body text.
    """
    
    implements(IDisclaimerText)
    
    def __init__(self, context):
        self.context = context
    
    def __call__(self):
        purl = getToolByName(self.context, 'portal_url')
        pobj = purl.getPortalObject()
        disc = pobj.get('disclaimer')
        if not disc:
            raise AttributeError(u'Disclaimer Object missing')
        if not IATDocument.providedBy(disc):
            raise AttributeError(u'Unknown Object declared as Disclaimer')
        return disc.getText()