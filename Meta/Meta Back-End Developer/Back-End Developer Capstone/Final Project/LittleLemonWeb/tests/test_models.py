from django.test import TestCase
from restaurant.models import Menu, Booking

#TestCase class
class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Greek Salad", price=6, inventory=100)
        self.assertEqual(str(item), 'Greek Salad : 6')