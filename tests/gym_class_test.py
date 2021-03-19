import unittest

from models.gym_class import Gym_Class

class TestGym_Class(unittest.TestCase):

    def setUp(self):
        self.class_1 = Gym_Class("Yoga", "Conditioning", "45 minutes", 15, "Low", "Moderate", "05/03/2021", "09:15", "Sky Blue Studio")

    def test_class_has_title(self):
        self.assertEqual("Yoga", self.class_1.title)

    def test_class_has_category(self):
        self.assertEqual("Conditioning", self.class_1.category)

    def test_class_has_duration(self):
        self.assertEqual("45 minutes", self.class_1.duration)

    def test_class_has_capacity(self):
        self.assertEqual(15, self.class_1.capacity)

    def test_class_has_intensity(self):
        self.assertEqual("Low", self.class_1.intensity)

    def test_class_has_difficulty(self):
        self.assertEqual("Moderate", self.class_1.difficulty)

    def test_class_has_date(self):
        self.assertEqual("05/03/2021", self.class_1.date)

    def test_class_has_time(self):
        self.assertEqual("09:15", self.class_1.time)

    def test_class_has_location(self):
        self.assertEqual("Sky Blue Studio", self.class_1.location)
