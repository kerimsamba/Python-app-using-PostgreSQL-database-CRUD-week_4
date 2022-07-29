import unittest

from models.owner  import Owner

class TestOwner(unittest.TestCase):
    def setUp(self):
        self.owner = Owner("Bing", "Crosby")

    def test_owner_has_first_name(self):
        self.assertEqual("Bing", self.owner.first_name)

    def test_owner_has_surname(self):
        self.assertEqual("Crosby", self.owner.surname)


