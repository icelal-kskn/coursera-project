from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer
import json

class MenuViewTest(TestCase):
    def test_getall(self):
        item = Menu.objects.create(title='Menu Item 1', price=10.99, inventory=1)
        serialized_data = MenuSerializer(Menu.objects.all(), many=True).data
        self.assertEqual(item.title, 'Menu Item 1')
        self.assertEqual(item.price, 10.99)
        self.assertEqual(item.inventory, 1)