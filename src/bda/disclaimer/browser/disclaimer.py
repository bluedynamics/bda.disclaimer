# -*- coding: utf-8 -*-

from zope.component.interfaces import ComponentLookupError

from zExceptions import Redirect
from cornerstone.browser.base import RequestMixin
from cornerstone.browser.base import XBrowserView
from plone.app.layout.viewlets.common import ViewletBase

from Products.CMFPlone.utils import getToolByName

from bda.disclaimer.interfaces import IDisclaimerText

__author__ = """Robert Niederreiter <rnix@squarewave.at>"""
__docformat__ = 'plaintext'

class DisclaimerViewlet(ViewletBase, RequestMixin):

    def update(self):
        self.accepted = self.cookievalue('_dc_acc')
    
    def render(self):
        if self.accepted \
          or self.request['ACTUAL_URL'].endswith('/@@disclaimer'):
            return ''
        purl = getToolByName(self.context, 'portal_url')
        pobj = purl.getPortalObject()
        raise Redirect, self.makeUrl(pobj, resource='@@disclaimer')

class DisclaimerPage(XBrowserView):

    def currentlang(self):
        plt = getToolByName(self.context, 'portal_languages')
        if not plt:
            return None
        return plt.getLanguageBindings()[0]
    
    def pagetitle(self):
        purl = getToolByName(self.context, 'portal_url')
        pobj = purl.getPortalObject()
        return pobj.title
    
    def checkdisclaimer(self):
        display = True
        if self.formvalue('_dc_accept') == '1' \
          and self.formvalue('_dc_submitted'):
            self.cookieset('_dc_acc', '1')
            display = False
        elif self.cookievalue('_dc_acc'):
            display = False
        if not display:
            purl = getToolByName(self.context, 'portal_url')
            pobj = purl.getPortalObject()
            url = pobj.absolute_url()
            raise Redirect, url
    
    def disclaimertext(self):
        try:
            return IDisclaimerText(self.context)()
        except ComponentLookupError, e:
            return 'No Disclaimer text registered. %s' % str(e)
        except AttributeError, e:
            return 'Disclaimer Text not provided properly. %s' % str(e)
