# -*- coding: utf-8 -*-

from zope.interface import Interface

__author__ = """Robert Niederreiter <rnix@squarewave.at>"""
__docformat__ = 'plaintext'

class IDisclaimerLayer(Interface):
    """Layer for the Disclaimer product.
    """

class IDisclaimerText(Interface):
    
    def __call__():
        """Return the text to be displayed at the disclaimer page.
        """