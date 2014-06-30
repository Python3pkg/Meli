#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import ng_meli
import sure
import requests
from datetime import datetime, timedelta


class RequestsMock(object):

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


class NGMeliTest(unittest.TestCase):

    def setUp(self):
        self.access_token = 'OUAHSODUHAOUDHAOUSHDAUOS'
        self.ngm = ng_meli.NGMeli(
            app_id='123',
            app_secret='123123',
            access_token=self.access_token,
            refresh_token='OUAHSODUHAOUDHAOUSHDAUOS',
            expires=datetime.now() + timedelta(days=1),
        )

    def test_user_access_token_expiration(self):
        self.ngm.user.valid().should.be.true
        self.ngm.user.expires = datetime.now() - timedelta(days=1)
        self.ngm.user.valid().should.be.falsy

    def test_url_serialize(self):
        self.ngm.user.url_serialize().should.be.equal('?access_token=%s' % self.access_token)

    def test_refresh_token(self):
        ng_meli.requests = RequestRefreshTokenMock()
        # vamos invalidar o expires do usuário
        self.ngm.user.access_token.should.be.equal(self.access_token) 
        self.ngm.user.expires = datetime.now() - timedelta(days=1)
        self.ngm.user.access_token.should.be.equal('MAIS_FAKE_QUE_A_DILMA')

    def test_create_test_user(self):
        ng_meli.requests = RequestCreateUserMock()
        user = self.ngm.create_test_user()
        user.should.have.key('id')
        user.should.have.key('password')
        user.should.have.key('site_status')
        user.should.have.key('nickname')


    def tear_down(self):
        ng_meli.requests = requests


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(NGMeliTest)
    unittest.TextTestRunner(verbosity=3).run(suite)