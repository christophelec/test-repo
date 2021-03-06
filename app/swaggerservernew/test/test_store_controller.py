# coding: utf-8

from __future__ import absolute_import

from swaggerservernew.models.body_2 import Body2
from swaggerservernew.models.inline_response_200_3 import InlineResponse2003
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestStoreController(BaseTestCase):
    """ StoreController integration test stubs """

    def test_delete_order(self):
        """
        Test case for delete_order

        Delete purchase order by ID
        """
        response = self.client.open('/v2/store/order/{orderId}'.format(orderId=2),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_inventory(self):
        """
        Test case for get_inventory

        Returns pet inventories by status
        """
        response = self.client.open('/v2/store/inventory',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_order_by_id(self):
        """
        Test case for get_order_by_id

        Find purchase order by ID
        """
        response = self.client.open('/v2/store/order/{orderId}'.format(orderId=10),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_place_order(self):
        """
        Test case for place_order

        Place an order for a pet
        """
        body = Body2()
        response = self.client.open('/v2/store/order',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
