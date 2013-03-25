==============
bda.disclaimer
==============

Protect a Plone Site with a Disclaimer.

Dependencies:
-------------

  * cornerstone.browser

Installation:
-------------

  Make dependencies and ``bda.disclaimer`` available to your Zope instance,
  create or join a Plone Site, go to ``portal_setup`` via ZMI and apply
  ``bda.disclaimer`` extension profile.

Provide the Disclaimer Text:
----------------------------

  To provide a disclaimer text, there must be an adapter which provides
  ``bda.disclaimer.interfaces.IDisclaimerText``. There exists a default
  implementation, which expects an ATDocument at the Plone Site root with
  Id ``disclaimer``. The Body Text of this Document is used then as disclaimer
  text.

Customization:
--------------

  To provide your own disclaimer page you have to override the browser page
  named ``disclaimer``. The easiest way to this is to bind the new page to
  ``IPloneSiteRoot``, since the original one is bound to ``*``. This way you
  avoid the use of an ``overrides.zcml``. 

Copyright and Contributions:
---------------------------

  Copyright 2008, Blue Dynamics Alliance, Austria - http://bluedynamics.com
  
  Agitator Websolutions - http://www.agitator.com
  
  Written by: Robert Niederreiter <rnix@squarewave.at>