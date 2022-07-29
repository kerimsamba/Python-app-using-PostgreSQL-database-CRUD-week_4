import unittest

from models.vet import Vet

class TestVet(unittest.TestCase):
    def setUp(self):
        self.vet = Vet("James", "Herriot")

    def test_vet_has_first_name(self):
        self.assertEqual("James", self.vet.first_name)

    def test_vet_has_surname(self):
        self.assertEqual("Herriot", self.vet.surname)