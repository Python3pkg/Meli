#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import requests
import urllib

# Some globals.
API_PATH = 'https://api.mercadolibre.com/'

class User(object):

    def __init__(self, access_token, refresh_token, expires, client_id, client_secret):
        self._access_token = access_token
        self._refresh_token = refresh_token
        self.expires = expires
        self.client_id = client_id
        self.client_secret

    def is_valid(self):
        """
        The access_token is valid?
        """
        if self.expires and self.expires < datetime.now():
            return True
        return False

    def url_serialize(self):
        """
        Build the necessary data to make a valid url, ain't that a bitch?
        """
        return '?%s' % urllib.urlencode(access_token=self._access_token)


    def refresh_token(self):
        """
        Refresh the token, if all goes well, return a tuple
        with the access_token and the refresh_token
        """
        payload = {
            'grant_type': 'refresh_token',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': refresh_token
        }
        response = request.post(API_PATH + 'oauth/token' + self.url_serialize(), data=payload)
        return response.json()

    @property
    def access_token(self):
        """
        Return the access token if it's valid, otherwise refresh it.
        """
        if not self.is_valid():
            self.refresh_token()
        return self._access_token


class Application(object):

    app_id = None
    app_secret = None

    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret

    def create_test_user(self):
        return {}


class NGMeli(object):
    """Here is where the fun starts! :D"""

    app_id = None
    app_secret = None

    user = None
    application = None

    def __init__(self, app_id, app_secret,
                 access_token=None, refresh_token=None, expires=None):

        self.application = Application(app_id, app_secret)
        if access_token and refresh_token and expires:
            self.user = User(access_token, refresh_token, expires)

    def post(self, path, data, **params):
        return self.make_request(path, "POST", data=data, params=params)
        
    def get(self, path, **params):
        return self.make_request(path, 'GET' **params)

    def make_request(self, path, method, data=None, params={}):
        """
        Build up the absolute path, make the request and returns it!
        Ff theres a payload send it up, if there is a user, build the path
        with the access_token GET parameter
        """
        total_path = self.get_path(partial_path)
        arguments = self.get_arguments(params, data)
        if self.user:
            path += self.user.url_serialize()
        response = getattr(request, method.lower())(path, total_path, **arguments)
        return response.json()

    def get_arguments(self, params, data):
        arguments = {}
        if data:
            arguments['data'] = data
        if params:
            arguments.update(params)
        return arguments

    def get_path(self, partial_path):
        """
        Thou shalt not leave the path
        """
        if not partial_path.startswith('/'):
            partial_path = '/' + partial_path
        return API_PATH + partial_path 








