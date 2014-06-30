#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import ng_meli
from datetime import datetime, timedelta

class RequestsMock(object):

    def post(self, *args, **kwargs):
        return self

    def json(self, *args, **kwargs):
        return {

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
        self.assertTrue(self.ngm.user.valid())
        self.ngm.user.expires = datetime.now() - timedelta(days=1)
        self.assertFalse(self.ngm.user.valid())

    def test_url_serialize(self):
        self.assertEqual(self.ngm.user.url_serialize(), '?access_token=%s' % self.access_token)

    def test_refresh_token(self):
        fake_access_token = 'MAIS_FAKE_QUE_A_DILMA' 
        # vamos invalidar o expires do usuário
        self.assertEqual(self.ngm.user.access_token, self.access_token)
        self.ngm.user.expires = datetime.now() - timedelta(days=1)





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(NGMeliTest)
    unittest.TextTestRunner(verbosity=3).run(suite)