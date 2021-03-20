import unittest

from models.gym_category import Gym_Category

class TestGym_Category(unittest.TestCase):
    def setUp(self):
        self.category_1 = Gym_Category("Conditioning")

    def test_category_has_category(self):
        self.assertEqual("Conditioning", self.category_1.category)