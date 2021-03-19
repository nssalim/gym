import unittest
from models.gym_booking import Gym_Booking
from models.gym_member import Gym_Member
from models.gym_class import Gym_Class
from models.gym_category import Gym_Category

class TestGymBookingClass(unittest.TestCase):
    def setUp(self):
        self.gym_member = Gym_Member("James", "Bond", 36, "30 Wellington Square, Chelsea", "02038805903", "james.bond@zoho.com", "True", "007", "True" )
        self.gym_class = Gym_Class("Yoga", "Conditioning", "45 minutes", 15, "Low", "Moderate", "05/03/2021", "09:15", "Sky Blue Studio")
        self.gym_category = Gym_Category("Conditioning")

    def test_can_test(self):
        self.assertEqual(True, True)


