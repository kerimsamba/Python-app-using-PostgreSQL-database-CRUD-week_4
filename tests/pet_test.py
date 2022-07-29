import unittest
import datetime

from models.pet import Pet

class TestPet(unittest.TestCase):
    def setUp(self):
        self.pet = Pet("Max", datetime.date(2015, 1, 1), "cat", "check up")

    def test_pet_has_name(self):
        self.assertEqual("Max", self.pet.name)

    def test_pet_has_dob(self):
        self.assertEqual(datetime.date(2015, 1, 1), self.pet.dob)

    def test_pet_has_type(self):
        self.assertEqual("cat", self.pet.type)

    def test_pet_has_been_treated(self):
        self.assertEqual("check up", self.pet.treatment_notes)












