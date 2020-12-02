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


member_1 = Gym_Member("John", "Jones", "22", "0/141 454 4231", "john.jones@hotmail.com")
gym_member_repository.save(member_1)

member_2 = Gym_Member("Paul" "Jackson", "34", "0/131 643 7567", "paul.jackson@mymail.com")
gym_member_repository.save(member_2)

member_3 = Gym_Member("Andrew" "Smith", "21", "0/121 123 456 7890", "ringo.smith@gmail.com")
gym_member_repository.save(member_3)

member_4 = Gym_Member("George" "Tucker", "54", "0/131 321 5464", "george.tucker@gmail.com")
gym_member_repository.save(member_4)
 
member_5 = Gym_Member("Kate", "Munro", "23", "0/141 980 8673", "kate.munro@yahoo.com")
gym_member_repository.save(member_4)

member_6 = Gym_Member("Joy" "Wilby", "50", "0/134 547 7310", "joy.wilby@hotmail.com")
gym_member_repository.save(member_4)

member_7 = Gym_Member("Andrew" "German", "31", "0/543 376 1209", "jane.german@gmail.com")
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

class_6 = Gym_Class("aerobics")
gym_class_repository.save(class_6)

class_7 = Gym_Class("box fit")
gym_class_repository.save(class_7)


booking_1 = Gym_Booking(member_1, class_1)
gym_booking_repository.save(booking_1)

booking_2 = Gym_Booking(member_2, class_2)
gym_booking_repository.save(booking_2)

booking_3 = Gym_Booking(member_3, class_3)
gym_booking_repository.save(booking_3)

booking_4 = Gym_Booking(member_4, class_1)
gym_booking_repository.save(booking_4)

booking_5 = Gym_Booking(member_1, class_2)
gym_booking_repository.save(booking_5)

booking_6 = Gym_Booking(member_2, class_5)
gym_booking_repository.save(booking_6)

booking_7 = Gym_Booking(member_4, class_4)
gym_booking_repository.save(booking_7)

booking_8 = Gym_Booking(member_3, class_6)
gym_booking_repository.save(booking_8)

booking_9 = Gym_Booking(member_4, class_7)
gym_booking_repository.save(booking_9)

booking_10 = Gym_Booking(member_4, class_2)
gym_booking_repository.save(booking_10)


pdb.set_trace()