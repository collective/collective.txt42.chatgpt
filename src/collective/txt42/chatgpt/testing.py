# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.txt42.chatgpt


class CollectiveTxt42ChatgptLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.txt42.chatgpt)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.txt42.chatgpt:default")


COLLECTIVE_TXT42_CHATGPT_FIXTURE = CollectiveTxt42ChatgptLayer()


COLLECTIVE_TXT42_CHATGPT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_TXT42_CHATGPT_FIXTURE,),
    name="CollectiveTxt42ChatgptLayer:IntegrationTesting",
)


COLLECTIVE_TXT42_CHATGPT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_TXT42_CHATGPT_FIXTURE,),
    name="CollectiveTxt42ChatgptLayer:FunctionalTesting",
)


COLLECTIVE_TXT42_CHATGPT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_TXT42_CHATGPT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CollectiveTxt42ChatgptLayer:AcceptanceTesting",
)
