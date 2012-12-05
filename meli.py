# -*- coding: utf -*-

import json
import requests
from urllib import urlencode
import logging
logging.basicConfig(filename='meli.log', level=logging.INFO)


class Meli(Object):

    access_token = None
    app_id = None
    app_secret = None
    base_url = 'https://api.mercadolibre.com/'

    def __init__(self, appid=None, appsecret=None):
        logging.info('initiating meli...')
        if appid:
            self.app_id = appid
        if appsecret:
            self.app_secret = appsecret

    def make_request(self, method='GET', path=None, data=None, **params):

        url = self.compose_url(path, **params)
        if method == 'GET':
            return requests.get(url)
        elif method == 'POST':
            return requests.post(url, data=data)
        else:
            logging.info('not yet supported')
            return False

    def compose_url(self, path, **params):
        if params:
            return self.base_url + path + '?' + urlencode(params)
        else:
            return self.base_url + path

    def get(self, path, **params):

        return self.make_request('GET', path, **params)





