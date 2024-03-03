from django.test import TestCase
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(Title="IceCream", price=80, inventory=100)
        itemstr = item.get_item()
        
        self.assertEqual(itemstr, "IceCream : 80")