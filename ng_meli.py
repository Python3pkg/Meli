#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import requests
import urllib

# Some globals.
API_PATH = 'https://api.mercadolibre.com'

class User(object):

    def __init__(self, access_token, refresh_token, expires, client_id, client_secret):
        self._access_token = access_token
        self._refresh_token = refresh_token
        self.expires = expires
        self.client_id = client_id
        self.client_secret = client_secret

    def valid(self):
        """
        The access_token is valid?
        """
        if self.expires and self.expires > datetime.now():
            return True
        return False

    def url_serialize(self):
        """
        Build the necessary data to make a valid url, ain't that a bitch?
        """
        return '?%s' % urllib.urlencode({"access_token": self._access_token})


    def refresh_token(self):
        """
        Refresh the token, if all goes well, return a tuple
        with the access_token and the refresh_token
        """
        payload = {
            'grant_type': 'refresh_token',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token
        }
        response = requests.post(API_PATH + 'oauth/token' + self.url_serialize(), data=payload)
        data = response.json()
        self._access_token = data['access_token']
        self._refresh_token = data['refresh_token']
        return data

    @property
    def access_token(self):
        """
        Return the access token if it's valid, otherwise refresh it.
        """
        if not self.valid():
            self.refresh_token()
        return self._access_token


class Application(object):

    app_id = None
    app_secret = None
    auth_url = 'http://auth.mercadolivre.com.br/'

    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret

    def create_test_user(self, access_token):
        payload = {
            'site_id': 'MLB'
        }
        response = requests.post(
            API_PATH + 'users/test_user?%s' % urllib.urlencode({'access_token': access_token}),
            data=payload)
        return response.json()

    def authorize_url(self):
        # For now, only suports mercadolivre.com.br, if you want somehow the login page
        # on your language, pull request is your friend.
        arguments = {
            'response_type':'code',
            'client_id': self.app_id
        }
        return self.auth_url + 'authorization?%s' % urllib.urlencode(arguments)


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
            self.user = User(access_token, refresh_token, expires, app_id, app_secret)

    def post(self, path, data=None, **params):
        return self.make_request(path, "POST", data=data, params=params)
        
    def get(self, path, **params):
        return self.make_request(path, 'GET' **params)

    def put(self, path, **params):
        return self.make_request(path, 'PUT' **params)

    def delete(self, path, **params):
        return self.make_request(path, 'DELETE' **params)

    def create_test_user(self, access_token=None):
        if not self.user:
            raise AttributeError('There is no user!') 
        return self.application.create_test_user(access_token=self.user.access_token)

    def make_request(self, path, method, data=None, params={}):
        """
        Build up the absolute path, make the request and returns it!
        Ff theres a payload send it up, if there is a user, build the path
        with the access_token GET parameter
        """
        total_path = self.get_path(path)
        arguments = self.get_arguments(params, data)
        if self.user:
            path += self.user.url_serialize()
        response = getattr(requests, method.lower())(total_path, **arguments)
        return response.json()

    def get_arguments(self, params, data):
        arguments = {}
        if data:
            arguments['data'] = data
        if params:
            arguments.update(params)
        return arguments

    def user_from_code(self, code, url_redirect):
        # oauth/token
        arguments = {
            'grant_type': 'authorization_code',
            'client_id': self.application.app_id,
            'client_secret': self.application.app_secret,
            'code': code,
            'redirect_uri': url_redirect
        }
        response = self.make_request(
            '/oauth/token?%s' % urllib.urlencode(arguments), 'POST')
        if 'access_token' in response:
            self.user = User(
                response['access_token'], response['refresh_token'],
                response['expires_in'], self.app_id, self.app_secret)
        return self

    def get_path(self, partial_path):
        """
        Thou shalt not leave the path.
        """
        if not partial_path.startswith('/'):
            partial_path = '/' + partial_path
        return API_PATH + partial_path 







