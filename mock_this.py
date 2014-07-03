# -*- coding: utf-8 -*-
"""
This file is responsible for the mocking stuff,
here all the mocking shall be done!
"""


class RequestsMock(object):
    text = True

    def post(self, *args, **kwargs):
        return self

    def get(self, *args, **kwargs):
        return self

    def json(self, *args, **kwargs):
        return self.mock()


class RequestRefreshTokenMock(RequestsMock):

    access_token = 'MAIS_FAKE_QUE_A_DILMA'

    def mock(self):
        return {
            'access_token': self.access_token,
            'refresh_token': 'NEW'
        }


class RequestCreateUserMock(RequestsMock):

    def mock(self):
        return {
            "id": 666,
            "nickname": "TESTE69",
            "password": "qatest328",
            "site_status": "active"
        }

class RequestAuthorizationMock(RequestsMock):

    def __init__(self, valid=True):
        self.valid = valid

    def mock(self):
        if self.valid:
            return { 
                "access_token" : "YOUR_NEW_ACCESS_TOKEN",
                "token_type" : "bearer",
                "expires_in" : 10800,
                "refresh_token" : "YOUR_REFRESH_TOKEN",
                "scope" : "write read offline_access"
            }
        else:
            return {
                u'cause': [],
                u'error': u'invalid_client',
                u'message': u'invalid client_id 123 or client_secret.',
                u'status': 400
            }