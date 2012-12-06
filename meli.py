# -*- coding: utf-8 -*-

import json
import requests
from urllib import urlencode
import sys
import logging
logging.basicConfig(filename='meli.log', level=logging.INFO)


# Errors...
class ValidationError(Exception):
    pass


class GenericError(Exception):
    pass


class Meli(object):

    access_token = None
    app_id = None
    app_secret = None
    base_url = 'https://api.mercadolibre.com/'
    data = None
    status = None

    def __init__(self, appid=None, appsecret=None):

        logging.info('initiating meli...')
        if appid:
            self.app_id = appid
        if appsecret:
            self.app_secret = appsecret

    def __nonzero__(self):

        if self.status not in [200, 201, 202, 204]:
            return False
        return True

    def make_request(self, method='GET', path=None, data=None, **params):

        url = self.compose_url(path, **params)
        if method == 'GET':
            self.data = self.parse_response(requests.get(url))
        elif method == 'POST':
            if isinstance(data, dict) or isinstance(data, list):
                try:
                    data = json.dumps(data)
                except:
                    logging.error('Invalid data?')
                    return self
            self.data = self.parse_response(requests.post(url, data=data))
        else:
            logging.info('not yet supported')
        return self

    def compose_url(self, path, **params):

        if params:
            if 'access' in params:
                if self.get_access_token():
                    params['access_token'] = self.get_access_token()
                else:
                    logging.warn('Empty or invalid access_token')
                params.pop('access')
                # joining the lists with ,
                for k, v in params.items():
                    if isinstance(v, list):
                        params[k] = ','.join(v)
            url = self.base_url + path + '?' + urlencode(params)
        else:
            url = self.base_url + path

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

    def raise_error(self, data):
        logging.info('Parsing error...')
        if not data:
            logging.info('Data is empty')
            return None

        if not self:
            logging.info('Yeah, we have a error!')
            name = self.parse_exception_name(data.get('message', 'Generic Error'))
            causes = ''
            for i in data.get('cause', []):
                causes += ' %s\n' % i.get('message', '')
            ex = getattr(sys.modules[__name__], name)(causes)

            raise ex

    def parse_exception_name(self, name):
        normalize_name = ''
        for i in name.split(' '):
            normalize_name += i.title()
        return normalize_name

    def parse_response(self, response):
        try:
            data = json.loads(response.text)
            # get the status from mercadolibre status code.
            self.status = data['status']
            logging.info('We got a json file!')

        except:
            # not json
            data = {
                'status': response.status_code,
                'data': response.text
            }
            # not a json file, get the HTTP status code instead.
            self.status = response.status_code

            # raise error?
        self.raise_error(data)
        return data
