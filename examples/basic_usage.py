#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-

from pyawairlocal.client import AwairClient
from pyawairlocal.data import get_dev_config, get_dev_data

test_dev = AwairClient(host='10.101.20.52')

get_dev_config(test_dev)

get_dev_data(test_dev)

