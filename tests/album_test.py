import unittest
from models.album import Album
from models.artist import Artist

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.artist1 = Artist("Michael Jackson")
        self.album1 = Album("Thriller", "Pop", self.artist1)

    def test_album_has_title(self):
        self.assertEqual("Thriller", self.album1.title)
    
    def test_album_has_genre(self):
        self.assertEqual("Pop", self.album1.genre)
    
    def test_album_has_artist(self):
        self.assertEqual(self.artist1, self.album1.artist)

    def test_album_has_id(self):
        self.assertEqual(None, self.album1.id)
