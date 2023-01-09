import unittest
from modules.room import Room
from modules.guest import Guest
from modules.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):

        self.song = Song("Minnie Riperton", "California Soul")

    def test_song_has_name(self):
        self.assertEqual("California Soul", self.song.song_name)
