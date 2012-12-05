# -*- coding: utf -*-

import json
import requests
from urllib import urlencode
import logging
logging.basicConfig(filename='meli.log', level=logging.INFO)


class Meli(object):

    access_token = None
    app_id = None
    app_secret = None
    base_url = 'https://api.mercadolibre.com'

    def __init__(self, appid=None, appsecret=None):
        logging.info('initiating meli...')
        if appid:
            self.app_id = appid
        if appsecret:
            self.app_secret = appsecret

    def make_request(self, method='GET', path=None, data=None, **params):

        url = self.compose_url(path, **params)
        if method == 'GET':
            return self.parse_response(requests.get(url))
        elif method == 'POST':
            return self.parse_response(requests.post(url, data=data))
        else:
            logging.info('not yet supported')
            return False

    def compose_url(self, path, **params):
        if params:
            if 'access' in params:
                params['access_token'] = self.get_access_token()
                params.pop('access')
            url = self.base_url + path + '?' + urlencode(params)
        else:
            url =  self.base_url + path

        logging.info(url)
        return url

    def get(self, path, **params):
        return self.make_request('GET', path, **params)

    def post(self, path, data=None, **params):
        return self.make_request('POST', path, data, **params)

    def get_access_token(self):
        if self.access_token:
            return self.access_token

    def set_access_token(self, token):
        self.access_token = token

    def parse_response(self, response):

        try:
            data = json.loads(response.text)
        except:
            # not json
            data = data

        output = {
            'status': response.status_code,
            'data':  data
        }

        return output
