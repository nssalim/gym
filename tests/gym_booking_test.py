import unittest
from models.gym_booking import Gym_Booking
from models.gym_member import Gym_Member
from models.gym_class import Gym_Class
from models.gym_category import Gym_Category

class TestGymBookingClass(unittest.TestCase):
    def setUp(self):
        self.member_1 = Gym_Member("James", "Bond", 36, "30 Wellington Square, Chelsea", "02038805903", "james.bond@zoho.com", "True", "007", "True" )
        self.class_1 = Gym_Class("Yoga", "45 minutes", 20, "Low", "Moderate", "05/03/2021", "09:15", "Sky Blue Studio")
        self.category_1 = Gym_Category("Flex and Core")
        self.booking_1 = Gym_Booking("James Bond",  "Yoga", "Flex and Core", 7, 20)

    def test_can_test(self):
        self.assertEqual(True, True)

    def test_booking_has_bookings(self):
        self.assertEqual(7, self.booking_1.bookings)

    def test_booking_has_booked_count(self):
        self.assertEqual(20, self.booking_1.booked_count)

    def test_booking_can_add_bookings(self):
        self.booking_1.bookings +=1
        self.assertEqual(8, self.booking_1.bookings)

    def test_booking_can_delete_bookings(self):
        self.booking_1.bookings -=1
        self.assertEqual(6, self.booking_1.bookings)

    def test_booking_has_member_name(self):
        self.assertEqual("James Bond", self.booking_1.gym_member)

    def test_booking_has_class_name(self):
        self.assertEqual("Yoga", self.booking_1.gym_class)

    def test_booking_has_category(self):
        self.assertEqual("Flex and Core", self.booking_1.gym_category)

    def test_booking_has_class_date(self):
        self.assertEqual("05/03/2021", self.class_1.date)

    def test_booking_has_class_time(self):
        self.assertEqual("09:15", self.class_1.time)
    
    def test_booking_has_class_duration(self):
        self.assertEqual("45 minutes", self.class_1.duration)