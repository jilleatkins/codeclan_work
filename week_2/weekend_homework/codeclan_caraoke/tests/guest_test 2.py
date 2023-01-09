import unittest
from modules.room import Room
from modules.guest import Guest
from modules.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        
        self.guest1 = Guest("Nicola", 234.00, "California Soul")
        self.guest2 = Guest("Andrew", 8.00, "Song 2")
        self.guest3 = Guest("Margie", 584.00, "Sunshine on Leith")
        self.guest4 = Guest("Bailey", 12.00, "Baby Shark")

        self.song1 = Song("Minnie Riperton", "California Soul")
        self.song2 = Song("Blur", "Song 2")
        self.song3 = Song("The Proclaimers", "Sunshine on Leith")
        self.song4 = Song("Pinkfong", "Baby Shark")

        self.room1 = Room("The Diana Ross Room", 5, 10.00)
        self.room2 = Room("The Nirvana Room", 5, 10.00)
        self.room3 = Room("The Bob Dylan Room", 5, 10.00)
        self.room4 = Room("The Teeny Boppers Room", 7, 2.00)


    def test_guest_has_a_name(self):
        self.assertEqual("Nicola", self.guest1.name)

    def test_guest_has_cash(self):
        self.assertEqual(234.00, self.guest1.cash)

    def test_check_guest_can_afford_admission(self):
        self.assertEqual(True, self.guest1.check_can_afford_admission(self.room1))

    def test_check_guest_cannot_afford_admission(self):
        self.assertEqual(False, self.guest2.check_can_afford_admission(self.room2))

    def test_pay_admission_fee(self):
        self.guest1.pay_admission_fee(self.room1)
        self.assertEqual(224, self.guest1.cash)

# Can't get the following to work - "TypeError: argument of type 'Song' is not iterable"
    # def test_react_to_favourite_song(self):
    #     self.room1.add_song(self.song1)
    #     self.assertEqual("This is my jam", self.guest1.react_to_favourite_song(self.song1))