# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.txt42.chatgpt.testing import (  # noqa: E501
    COLLECTIVE_TXT42_CHATGPT_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.txt42.chatgpt is properly installed."""

    layer = COLLECTIVE_TXT42_CHATGPT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if collective.txt42.chatgpt is installed."""
        self.assertTrue(self.installer.is_product_installed("collective.txt42.chatgpt"))

    def test_browserlayer(self):
        """Test that ICollectiveTxt42ChatgptLayer is registered."""
        from collective.txt42.chatgpt.interfaces import ICollectiveTxt42ChatgptLayer
        from plone.browserlayer import utils

        self.assertIn(ICollectiveTxt42ChatgptLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_TXT42_CHATGPT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("collective.txt42.chatgpt")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.txt42.chatgpt is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("collective.txt42.chatgpt")
        )

    def test_browserlayer_removed(self):
        """Test that ICollectiveTxt42ChatgptLayer is removed."""
        from collective.txt42.chatgpt.interfaces import ICollectiveTxt42ChatgptLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICollectiveTxt42ChatgptLayer, utils.registered_layers())
