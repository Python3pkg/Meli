#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import meli
import random
import time

globals()['product_id'] = None
globals()['user'] = None


class BasicMeliTests(unittest.TestCase):

    def setUp(self):

        self.access_token = "APP_USR-6614781133758051-121410-81308abe0ff18301e27e2d8be66077e3__C_N__-79576867"
        self.meli = meli.Meli(access_token=self.access_token)

    def test_001_create_test_user(self):
        usuario = {
            'site_id': 'MLB'
        }
        user = self.meli.post('users/test_user', usuario, access=True)
        self.assertTrue(user)
        globals()['user'] = user

    def test_002_product_not_found(self):

        product = self.meli.get('items/MLUHASUDO')
        self.assertFalse(product)
        self.assertEqual(product.status_code, 404)
        self.assertEqual(product.data.get('error'), 'not_found')
        self.assertEqual(product.data.get('message'), 'Item with id MLUHASUDO not found.')

    # def test_003_get_categorie(self):
    #     Category = self.meli.get('categories/MLB1499')
    #     categorie_json = {u'permalink': u'http://home.mercadolivre.com.br/agro-industria-comercio', u'name': u'Agro, Ind\xfastria e Com\xe9rcio', u'children_categories': [{u'total_items_in_this_category': 20279, u'id': u'MLB5452', u'name': u'Com\xe9rcio'}, {u'total_items_in_this_category': 10193, u'id': u'MLB1500', u'name': u'Constru\xe7\xe3o'}, {u'total_items_in_this_category': 11665, u'id': u'MLB2467', u'name': u'Energia El\xe9trica'}, {u'total_items_in_this_category': 11491, u'id': u'MLB2102', u'name': u'Equipamento para Escrit\xf3rios'}, {u'total_items_in_this_category': 20440, u'id': u'MLB5226', u'name': u'Ferramentas'}, {u'total_items_in_this_category': 6574, u'id': u'MLB1512', u'name': u'Ind\xfastria Agr\xedcola'}, {u'total_items_in_this_category': 3362, u'id': u'MLB1508', u'name': u'Ind\xfastria Automotiva'}, {u'total_items_in_this_category': 7763, u'id': u'MLB5446', u'name': u'Ind\xfastria Gr\xe1fica e Impress\xe3o'}, {u'total_items_in_this_category': 15308, u'id': u'MLB5456', u'name': u'Ind\xfastria Pesada'}, {u'total_items_in_this_category': 5636, u'id': u'MLB1504', u'name': u'Ind\xfastria Pl\xe1stica e Qu\xedmica'}, {u'total_items_in_this_category': 8900, u'id': u'MLB5454', u'name': u'Ind\xfastria T\xeaxtil e Confec\xe7\xe3o'}, {u'total_items_in_this_category': 8877, u'id': u'MLB5550', u'name': u'Medi\xe7\xf5es e Instrumenta\xe7\xe3o'}, {u'total_items_in_this_category': 10819, u'id': u'MLB1893', u'name': u'Outros'}, {u'total_items_in_this_category': 739, u'id': u'MLB6416', u'name': u'Reciclagem'}], u'settings': {u'rounded_address': False, u'vip_subdomain': u'produto', u'shipping_modes': [u'custom', u'me1', u'not_specified'], u'tags': [], u'simple_shipping': u'optional', u'coverage_areas': u'not_allowed', u'adult_content': False, u'mirror_category': None, u'seller_contact': u'not_allowed', u'stock': u'required', u'currencies': [u'BRL'], u'minimum_price': None, u'price': u'required', u'max_pictures_per_item': 6, u'immediate_payment': u'optional', u'items_reviews_allowed': False, u'shipping_profile': u'optional', u'maximum_price': None, u'shipping_options': [u'custom'], u'listing_allowed': False, u'show_contact_information': False, u'buying_modes': [u'auction', u'buy_it_now'], u'item_conditions': [u'new', u'not_specified', u'used'], u'buying_allowed': True}, u'total_items_in_this_category': 142046, u'path_from_root': [{u'id': u'MLB1499', u'name': u'Agro, Ind\xfastria e Com\xe9rcio'}], u'id': u'MLB1499'}
    #     self.assertTrue(Category)
    #     self.assertDictEqual(Category.data, categorie_json)

    def test_004_categorie_not_found(self):

        Category = self.meli.get('categories/OHASODUHASD')
        self.assertFalse(Category)
        self.assertEqual(Category.status_code, 404)
        self.assertEqual(Category.data['error'], 'not_found')
        self.assertEqual(Category.data.get('message'), 'Category not found: OHASODUHASD')

    def test_005_validate_product(self):
        product_data = {
            "title": "Arduino UNO",
            "category_id": "MLB11615",
            "price": 190,
            "currency_id": "BRL",
            "available_quantity": 1,
            "buying_mode": "buy_it_now",
            "listing_type_id": "free",
            "condition": "new",
            "description": "Arduino UNO novo na caixa com cabo e fonte.",
            "pictures": [
                {"source": "http://arduino.cc/en/uploads/Main/ArduinoUnoFront450px.jpg"},
                {"source": "http://www.liquidware.com/system/0000/3654/Arduino_Uno_Unboxing.jpg"}
            ]
        }

        Product = self.meli.post('items/validate', data=product_data, access=True)
        self.assertTrue(Product)
        self.assertEqual(Product.status_code, 204)

    def test_006_validate_product_wrong_category(self):

        product_data = {
            "title": "Arduino UNO",
            "category_id": "MLB1499",
            "price": 190,
            "currency_id": "BRL",
            "available_quantity": 1,
            "buying_mode": "buy_it_now",
            "listing_type_id": "free",
            "condition": "new",
            "description": "Arduino UNO novo na caixa com cabo e fonte.",
            "pictures": [
                {"source": "http://arduino.cc/en/uploads/Main/ArduinoUnoFront450px.jpg"},
                {"source": "http://www.liquidware.com/system/0000/3654/Arduino_Uno_Unboxing.jpg"}
            ]
        }
        with self.assertRaises(meli.ValidationError):
            self.meli.post('items/validate', data=product_data, access=True)

    def test_007_create_product(self):

        product_data = {
            "title": "Arduino Uno - Teste",
            "category_id": "MLB11615",
            "price": 190,
            "currency_id": "BRL",
            "available_quantity": 1,
            "buying_mode": "buy_it_now",
            "listing_type_id": "free",
            "condition": "new",
            "description": "Arduino Uno novo na caixa com cabo e fonte.",
            "pictures": [
                {"source": "http://arduino.cc/en/uploads/Main/ArduinoUnoFront450px.jpg"},
                {"source": "http://www.liquidware.com/system/0000/3654/Arduino_Uno_Unboxing.jpg"}
            ]
        }

        new_product = self.meli.post('items/', product_data, access=True)
        self.assertTrue(new_product)
        globals()['product_id'] = new_product.data['id']

        product = self.meli.get('items/%s' % new_product.data.get('id'))

        for k, v in product_data.items():
            if not isinstance(v, list):
                self.assertEqual(v, product.data.get(k))

    def test_008_question(self):
        question_data = {
            'item_id': globals()['product_id'],

            'text': "Mussum ipsum cacilds, vidis litro abertis. Consetis adipiscings elitis. Pra lá."
        }
        question = self.meli.post('questions', question_data, access=True)
        self.assertTrue(question)

        # answering...
        answer_data = {
            'question_id': question.data.get('id'),
            'text': ' i pareci latim. Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis.'
        }

        answer = self.meli.post('answer', answer_data, access=True)
        self.assertTrue(answer)

    def test_008_modify_price_item(self):
        preco = random.choice(range(250, 350))
        product_modify = {
            'price': preco
        }
        Product = self.meli.put('items/%s' % globals()['product_id'], product_modify, access=True)
        self.assertTrue(Product)
        self.assertEqual(Product.data['price'], preco)

    def test_finish_product(self):
        while True:
            Product = self.meli.get('items/%s' % globals()['product_id'])
            if Product.data.get('status') != 'not_yet_active':
                break
            time.sleep(5)
        status = {
            'status': 'closed'
        }
        self.meli.put('items/%s' % globals()['product_id'], data=status, access=True)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BasicMeliTests)
    unittest.TextTestRunner(verbosity=3).run(suite)
