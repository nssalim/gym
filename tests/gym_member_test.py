import unittest

from models.gym_member import Gym_Member

class TestGym_Member(unittest.TestCase):

    def setUp(self):
        self.member_1 = Gym_Member("James", "Bond", 36, "30 Wellington Square, Chelsea", "02038805903", "james.bond@zoho.com", "True", "007", "True")

    def test_member_has_first_name(self):
        self.assertEqual("James", self.member_1.first_name)

    def test_member_has_last_name(self):
        self.assertEqual("Bond", self.member_1.last_name)

    def test_member_has_age(self):
        self.assertEqual(36, self.member_1.age)

    def test_member_has_address(self):
        self.assertEqual("30 Wellington Square, Chelsea", self.member_1.address)

    def test_member_has_phone_no(self):
        self.assertEqual("02038805903", self.member_1.phone_no)

    def test_member_has_email(self):
        self.assertEqual("james.bond@zoho.com", self.member_1.email)

    def test_member_has_premium(self):
        self.assertEqual("True", self.member_1.premium)

    def test_member_has_membership_no(self):
        self.assertEqual("007", self.member_1.membership_no)

    def test_member_is_active(self):
        self.assertEqual("True", self.member_1.is_active)