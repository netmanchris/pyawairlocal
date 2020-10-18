# -*- coding: utf-8 -*-
"""
Module for testing the functions in pyawairlocal.data.
"""

import os
import vcr
from unittest import TestCase
from unittest import mock
from nose.plugins.skip import SkipTest

from pyawairlocal.client import AwairClient
from pyawairlocal.data import get_dev_config, get_dev_data

awair_dev = os.environ['OMNI_IP']

test_dev = AwairClient(host=awair_dev)

my_vcr = vcr.VCR(
    serializer='json',
    cassette_library_dir='./test_pyhpecfm/fixtures/cassettes',
    record_mode='new_episodes',
    match_on=['uri', 'method'],
)

class TestGetDevConfig(TestCase):
    """
    Test Case for pyawairlocal.data.get_dev_config function
    """

    @vcr.use_cassette(cassette_library_dir='./test_pyyawairlocal/fixtures/cassettes')
    def test_get_dev_config(self):
        """
        Simple test to return dev_config. URL has no parameters
        :return:
        """
        dev_config = get_dev_config(test_dev)
        my_attributes = ['device_uuid', 'wifi_mac', 'ip', 'netmask', 'gateway', 'fw_version', 'timezone', 'display', 'led', 'power-status']
        self.assertIs(type(dev_config),dict)
        for i in dev_config.keys():
            self.assertIn(i,my_attributes)