import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Tennents", 5, 4)

    # @unittest.skip('skipped')
    def test_drink_has_name(self):
        self.assertEqual("Tennents", self.drink.name)

    # @unittest.skip('skipped')
    def test_drink_has_price(self):
        self.assertEqual(5, self.drink.price)

    @unittest.skip('skipped')
    def test_drink_has_alcohol_level(self):
        self.assertEqual(4, self.drink.alcohol)

    

    

    
