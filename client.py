#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module provides helper functions and holds the main client object
for authenticating with an HPE Composable Fabric Manager.
"""
import time

import requests

# The following lines remove warnings for self-signed certificates
# noinspection PyUnresolvedReferences
from requests.packages.urllib3.exceptions import \
    InsecureRequestWarning  # pylint: disable=import-error

# noinspection PyUnresolvedReferences
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # pylint: disable=no-member


class AwairApiError(Exception):
    """Awair Local API exception."""
    pass


class AwairClient(object):
    """Client class for the Awair Local REST API bindings."""

    def __init__(self, host, verify_ssl=False, timeout=30):
        """
        Initialize API instance.

        :param host: str FQDN or IPv4 Address of the target Awair Local host
        :param verify_ssl: bool verify SSL certificate. Default value is False
        :param timeout: int timeout in seconds for API calls
        """
        self._host = host
        self._verify_ssl = verify_ssl
        self._timeout = timeout
        self._max_connection_retries = 3
        self._session = requests.Session()

    def get(self, path, params=None):
        """
        Helper function for HTTP GET commands

        :param params:
        :param path: str the requested path
        :return: requests.Response API call response
        :rtype: requests.Response
        """
        return self._call_api(method='GET', path=path, params=params)

    def patch(self, path, data):
        """
        Helper function for HTTP PATCH commands

        :param path: str the requested path
        :param data: dict the data to send
        :return: requests.Response API call response
        :rtype: requests.Response
        """
        return self._call_api(method='PATCH', path=path, json=data)

    def post(self, path, params=None, data=None):
        """
        Helper function for HTTP POST commands

        :param data:
        :param params:
        :param path: str the requested path
        :return: requests.Response API call response
        :rtype: requests.Response
        """
        return self._call_api(method='POST', path=path, params=params, json=data)

    def put(self, path, data):
        """
        Helper function for HTTP PUT commands

        :param path: str the requested path
        :param data: dict the data to send
        :return: requests.Response API call response
        :rtype: requests.Response
        """
        return self._call_api(method='PUT', path=path, json=data)

    def _call_api(self, method, path, params=None, headers=None, data=None, json=None,
                  timeout=None, stream=False):
        """Execute an Awair Local Device REST API request.

        Arguments:
            method (str): HTTP request type
            path (str): The request path of the Awair Local REST API.
            params (dict): (Optional) query parameters.
            headers (dict): (Optional) HTTP Headers to send with the request.
            json (dict): (Optional) json to send in the body of the request.
            timeout (int): Optional timeout override.

        Returns:
            requests.Response (class): JSON representation of the response object from requests
        """
        request_headers = headers if headers else {'Content-Type': 'application/json;charset=UTF-8'}
        attempts = 0
        url = 'http://{}/{}'.format(self._host, path)
        req = requests.Request(method=method, url=url, data=data, headers=headers)
        prepped = self._session.prepare_request(req)
        return self._session.send(prepped)

