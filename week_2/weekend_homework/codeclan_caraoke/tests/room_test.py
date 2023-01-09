import unittest
from modules.room import Room
from modules.guest import Guest
from modules.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.guest1 = Guest("Nicola", 234.00, "California Soul")
        self.guest2 = Guest("Andrew", 53.00, "Song 2")
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


    def test_room_has_a_name(self):
        self.assertEqual("The Diana Ross Room", self.room1.name)

    def test_get_room_capacity(self):
        self.assertEqual(5, self.room1.capacity)

    def test_get_room_guests(self):
        self.assertEqual(0, len(self.room1.guests))

    def test_get_room_admission_fee(self):
        self.assertEqual(10.00, self.room1.admission_fee)

    def add_guest(self, guest):
        self.room1.guests.append(guest)

    def remove_guest(self, guest):
        self.room1.guests.remove(guest)

    def test_get_song_count(self):
        self.assertEqual(0, len(self.room1.song_list))

    def test_add_song_to_room(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.song_list))

    def test_play_song(self):
        self.room1.add_song(self.song1)

        
