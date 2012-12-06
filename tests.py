#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import meli
import random
import time

globals()['product_id'] = None

class BasicMeliTests(unittest.TestCase):

    def setUp(self):

        self.access_token = 'APP_USR-3975401489804986-120613-5a8004f28c883e8ea0d7361757bf20ff__I_L__-79576867'
        self.meli = meli.Meli(access_token=self.access_token)

    def test_001_get_product(self):
        product = self.meli.get('items/MLB436812852')
        product_json = {u'warranty': u'3 Meses', u'geolocation': {u'latitude': u'', u'longitude': u''}, u'subtitle': u'Somos Mercado L\xedder Platinum! Compra 100% Garantida', u'site_id': u'MLB', u'buying_mode': u'buy_it_now', u'currency_id': u'BRL', u'descriptions': [{u'id': u'MLB436812852-282175130'}], u'last_updated': u'2012-10-29T11:42:43.000Z', u'id': u'MLB436812852', u'title': u'Xbox 360 Slim Arcade 4gb Pronto Para O Kinect Original Hdmi', u'pictures': [{u'secure_url': u'https://www.mercadolibre.com/jm/img?s=MLB&v=O&f=222366190_8699.jpg', u'url': u'http://img1.mlstatic.com/s_MLB_v_O_f_222366190_8699.jpg', u'quality': u'', u'id': u'MLB222366190_8699', u'max_size': u'250x250', u'size': u'250x250'}, {u'secure_url': u'https://www.mercadolibre.com/jm/img?s=MLB&v=O&f=222366190_6364.jpg', u'url': u'http://img2.mlstatic.com/s_MLB_v_O_f_222366190_6364.jpg', u'quality': u'', u'id': u'MLB222366190_6364', u'max_size': u'250x250', u'size': u'250x250'}, {u'secure_url': u'https://www.mercadolibre.com/jm/img?s=MLB&v=O&f=222366190_7349.jpg', u'url': u'http://img2.mlstatic.com/s_MLB_v_O_f_222366190_7349.jpg', u'quality': u'', u'id': u'MLB222366190_7349', u'max_size': u'250x250', u'size': u'250x250'}, {u'secure_url': u'https://www.mercadolibre.com/jm/img?s=MLB&v=O&f=222366190_9396.jpg', u'url': u'http://img2.mlstatic.com/s_MLB_v_O_f_222366190_9396.jpg', u'quality': u'', u'id': u'MLB222366190_9396', u'max_size': u'250x250', u'size': u'250x250'}, {u'secure_url': u'https://www.mercadolibre.com/jm/img?s=MLB&v=O&f=222366190_3139.jpg', u'url': u'http://img1.mlstatic.com/s_MLB_v_O_f_222366190_3139.jpg', u'quality': u'', u'id': u'MLB222366190_3139', u'max_size': u'250x250', u'size': u'250x250'}], u'coverage_areas': [], u'stop_time': u'2012-10-29T11:36:12.000Z', u'price': 749.89, u'seller_contact': None, u'location': None, u'status': u'closed', u'parent_item_id': u'MLB429513233', u'tags': [], u'start_time': u'2012-08-30T11:36:12.000Z', u'permalink': u'http://produto.mercadolivre.com.br/MLB-436812852-xbox-360-slim-arcade-4gb-pronto-para-o-kinect-original-hdmi-_JM', u'date_created': u'2012-08-30T11:36:12.000Z', u'accepts_mercadopago': True, u'available_quantity': 11, u'condition': u'new', u'sub_status': [u'expired'], u'seller_id': 38549536, u'catalog_product_id': None, u'seller_address': {u'comment': u'', u'city': {u'id': u'', u'name': u'SAO CAETANO DO SUL'}, u'country': {u'id': u'BR', u'name': u'Brasil'}, u'longitude': u'', u'state': {u'id': u'BR-SP', u'name': u'S\xe3o Paulo'}, u'latitude': u'', u'address_line': u'', u'id': 69872109, u'zip_code': u''}, u'video_id': u's2LBnBmdHGM', u'variations': [], u'non_mercado_pago_payment_methods': [{u'type': u'G', u'id': u'MLBWC', u'description': u'A combinar'}, {u'type': u'N', u'id': u'MLBCC', u'description': u'Cart\xe3o de Cr\xe9dito'}, {u'type': u'G', u'id': u'MLBMO', u'description': u'Dinheiro'}, {u'type': u'D', u'id': u'MLBDE', u'description': u'Dep\xf3sito Banc\xe1rio'}], u'shipping': {u'free_shipping': False, u'dimensions': None, u'profile_id': None, u'mode': u'custom', u'local_pick_up': True, u'methods': []}, u'thumbnail': u'http://img1.mlstatic.com/s_MLB_v_I_f_222366190_8699.jpg', u'sold_quantity': 308, u'listing_type_id': u'gold', u'attributes': [], u'category_id': u'MLB58427', u'initial_quantity': 200, u'base_price': 749.89}
        self.assertTrue(product)
        self.assertDictEqual(product.data, product_json)

    def test_002_product_not_found(self):

        product = self.meli.get('items/MLUHASUDO')
        self.assertFalse(product)
        self.assertEqual(product.status_code, 404)
        self.assertEqual(product.data.get('error'), 'not_found')
        self.assertEqual(product.data.get('message'), 'Item with id MLUHASUDO not found.')

    def test_003_get_categorie(self):
        Category = self.meli.get('categories/MLB1499')
        categorie_json = {u'permalink': u'http://home.mercadolivre.com.br/agro-industria-comercio', u'name': u'Agro, Ind\xfastria e Com\xe9rcio', u'children_categories': [{u'total_items_in_this_category': 20279, u'id': u'MLB5452', u'name': u'Com\xe9rcio'}, {u'total_items_in_this_category': 10193, u'id': u'MLB1500', u'name': u'Constru\xe7\xe3o'}, {u'total_items_in_this_category': 11665, u'id': u'MLB2467', u'name': u'Energia El\xe9trica'}, {u'total_items_in_this_category': 11491, u'id': u'MLB2102', u'name': u'Equipamento para Escrit\xf3rios'}, {u'total_items_in_this_category': 20440, u'id': u'MLB5226', u'name': u'Ferramentas'}, {u'total_items_in_this_category': 6574, u'id': u'MLB1512', u'name': u'Ind\xfastria Agr\xedcola'}, {u'total_items_in_this_category': 3362, u'id': u'MLB1508', u'name': u'Ind\xfastria Automotiva'}, {u'total_items_in_this_category': 7763, u'id': u'MLB5446', u'name': u'Ind\xfastria Gr\xe1fica e Impress\xe3o'}, {u'total_items_in_this_category': 15308, u'id': u'MLB5456', u'name': u'Ind\xfastria Pesada'}, {u'total_items_in_this_category': 5636, u'id': u'MLB1504', u'name': u'Ind\xfastria Pl\xe1stica e Qu\xedmica'}, {u'total_items_in_this_category': 8900, u'id': u'MLB5454', u'name': u'Ind\xfastria T\xeaxtil e Confec\xe7\xe3o'}, {u'total_items_in_this_category': 8877, u'id': u'MLB5550', u'name': u'Medi\xe7\xf5es e Instrumenta\xe7\xe3o'}, {u'total_items_in_this_category': 10819, u'id': u'MLB1893', u'name': u'Outros'}, {u'total_items_in_this_category': 739, u'id': u'MLB6416', u'name': u'Reciclagem'}], u'settings': {u'rounded_address': False, u'vip_subdomain': u'produto', u'shipping_modes': [u'custom', u'me1', u'not_specified'], u'tags': [], u'simple_shipping': u'optional', u'coverage_areas': u'not_allowed', u'adult_content': False, u'mirror_category': None, u'seller_contact': u'not_allowed', u'stock': u'required', u'currencies': [u'BRL'], u'minimum_price': None, u'price': u'required', u'max_pictures_per_item': 6, u'immediate_payment': u'optional', u'items_reviews_allowed': False, u'shipping_profile': u'optional', u'maximum_price': None, u'shipping_options': [u'custom'], u'listing_allowed': False, u'show_contact_information': False, u'buying_modes': [u'auction', u'buy_it_now'], u'item_conditions': [u'new', u'not_specified', u'used'], u'buying_allowed': True}, u'total_items_in_this_category': 142046, u'path_from_root': [{u'id': u'MLB1499', u'name': u'Agro, Ind\xfastria e Com\xe9rcio'}], u'id': u'MLB1499'}
        self.assertTrue(Category)
        self.assertDictEqual(Category.data, categorie_json)

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

        Product = self.meli.post('items/', product_data, access=True)
        self.assertTrue(Product)
        globals()['product_id'] = Product.data['id']

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
