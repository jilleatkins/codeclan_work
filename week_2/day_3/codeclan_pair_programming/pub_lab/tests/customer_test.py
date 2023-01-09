import unittest
from src.customer import Customer
from src.drinks import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Josh", 10, 92)
        self.drink = Drink("Guinness", 6, 5)

    # @unittest.skip('skipped')
    def test_is_customer(self):
        self.assertEqual("Josh", self.customer.name)
        self.assertEqual(10, self.customer.wallet)
        self.assertEqual(92, self.customer.age)

    # @unittest.skip('skipped')
    def test_decrease_wallet(self):
        self.customer.decrease_wallet(6)
        self.assertEqual(self.customer.wallet, 4)

    # @unittest.skip('skipped')
    def test_increase_drunkenness(self):
        self.customer.increase_drunkenness(self.drink)
        self.assertEqual(self.customer.drunkenness, 5)
