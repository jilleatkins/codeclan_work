import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink("Tennents", 5, 4)
        self.drink2 = Drink("Guinness", 6, 5)
        self.drinks =[self.drink1, self.drink2]
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub.drinks.extend(self.drinks)
        self.customer = Customer("Josh", 10, 92)
        self.customer_underage = Customer("Jill", 10, 15)

    def test_is_pub(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
        self.assertEqual(self.pub.till, 100.00)
        self.assertEqual(2, len(self.pub.drinks))

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual (102.50, self.pub.till)

    def test_check_age_true(self):
        test_result = self.pub.check_age(self.customer)
        self.assertEqual(True, test_result)

    def test_check_age_false(self):
        test_result = self.pub.check_age(self.customer_underage)
        self.assertEqual(False, test_result)

    def test_buy_drink_true(self):
        self.pub.serve_drink(self.customer, self.drink2)
        self.assertEqual(106.00, self.pub.till)
        self.assertEqual(4, self.customer.wallet)

    def test_buy_drink_false(self):
        self.pub.serve_drink(self.customer_underage, self.drink2)
        # self.pub.check_age(self.customer)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(10, self.customer_underage.wallet)
        
        
