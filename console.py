import pdb

from models.gym_booking import Gym_Booking
import repositories.gym_booking_repository as gym_booking_repository

from models.gym_class import Gym_Class
import repositories.gym_class_repository as gym_class_repository

from models.gym_member import Gym_Member
import repositories.gym_member_repository as gym_member_repository

gym_booking_repository.delete_all()
gym_class_repository.delete_all()
gym_member_repository.delete_all()

member_1 = Gym_Member("Jane")
gym_member_repository.save(member_1)

member_2 = Gym_Member("Peter")
gym_member_repository.save(member_2)

member_3 = Gym_Member("John")
gym_member_repository.save(member_3)

member_4 = Gym_Member("Joy")
gym_member_repository.save(member_4)

class_1 = Gym_Class("yoga")
gym_class_repository.save(class_1)

class_2 = Gym_Class("pilates")
gym_class_repository.save(class_2)

class_3 = Gym_Class("circuit class")
gym_class_repository.save(class_3)

class_4 = Gym_Class("zumba")
gym_class_repository.save(class_4)

class_5 = Gym_Class("cycle class")
gym_class_repository.save(class_5)



booking_1 = Gym_Booking(member_1, class_1)
gym_booking_repository.save(booking_1)

booking_1 = Gym_Booking(member_4, class_1)
gym_booking_repository.save(booking_4)


booking_2 = Gym_Booking(member_2, class_2)
gym_booking_repository.save(booking_2)


booking_3 = Gym_Booking(member_3, class_3)
gym_booking_repository.save(booking_1)


pdb.set_trace()