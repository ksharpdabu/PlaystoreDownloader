#!/usr/bin/env python
# coding: utf-8

import pytest

from playstore.playstore import Playstore
# noinspection PyUnresolvedReferences
from test.test_session_fixtures import credentials_path

VALID_PACKAGE_NAME = 'com.spotify.music'
BAD_PACKAGE_NAME = '<-bad_package_name->'


# noinspection PyShadowingNames
@pytest.fixture(scope='class')
def playstore(credentials_path):
    return Playstore(credentials_path)


# noinspection PyShadowingNames
class TestPlaystore(object):

    def test_valid_app_details(self, playstore):
        assert playstore.app_details(VALID_PACKAGE_NAME).docV2.docid == VALID_PACKAGE_NAME

    def test_bad_app_details(self, playstore):
        assert playstore.app_details(BAD_PACKAGE_NAME) is None
