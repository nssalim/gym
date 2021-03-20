import pdb

from models.gym_booking import Gym_Booking
import repositories.gym_booking_repository as gym_booking_repository

from models.gym_class import Gym_Class
import repositories.gym_class_repository as gym_class_repository

from models.gym_member import Gym_Member
import repositories.gym_member_repository as gym_member_repository

from models.gym_category import Gym_Category
import repositories.gym_category_repository as gym_category_repository


#CLEAR DATA from Tables
gym_booking_repository.delete_all()
gym_class_repository.delete_all()
gym_member_repository.delete_all()
gym_category_repository.delete_all()

#MEMBERS - Populate Member Table
member_1 = Gym_Member("James", "Bond", 36, "30 Wellington Square, Chelsea", "02038805903", "james.bond@zoho.com", "True", "007", "True")
gym_member_repository.save(member_1)

member_2 = Gym_Member("sherlock", "Holmes", 40, "221b Baker Street","02087047780", "sherlock.holmes@outlook.com", "True", "221", "False")
gym_member_repository.save(member_2)

member_3 = Gym_Member("Bridget", "Jones", 26, "8 Bedale Street", "02038696256", "bridget.jones@mail.com", "True", "003", "False")
gym_member_repository.save(member_3)

member_4 = Gym_Member("Hercule", "Poirot",  58, "56B Whitehavens Mansions",  "02083473422", "hercule.poirot@aol.com", "False", "300", "False")
gym_member_repository.save(member_4)

member_5 = Gym_Member("Mary", "Poppins", 29, "17 Cherry Tree Lane", "02084972723", "mary.poppins@gmail.com", "True", "004", "True")
gym_member_repository.save(member_5)

member_6 = Gym_Member("Count", "Dracula", 121, "Eon House, 138 Piccadilly",  "02037444469",  "count.dracula@mail.com", "True", "666", "False")
gym_member_repository.save(member_6)

member_7 = Gym_Member("Great Uncle Bulgaria", "Womble",  63, "6 Wimbledon Common", "02088361453", "greatunclebulgaria.womble@hotmail.com", "False", "100", "False")
gym_member_repository.save(member_7)

member_8 = Gym_Member("Paddington", "Bear", 12, "32 Windsor Gardens",  "02033150554", "paddington.bear@yahoo.com", "False", "400", "False")
gym_member_repository.save(member_8)

member_9 = Gym_Member("Dr Henry", "Jekyl", 44, "28 Leicester Square", "02031892862", "henry.jekyl@gmail.com", "True", "002", "False")
gym_member_repository.save(member_9)
 
member_10 = Gym_Member("Phileas", "Fogg", 31, "7 Savile Row, Burlington Gardens",  "02086187613", "phileas.fogg@btinternet.com", "True", "080", "False")
gym_member_repository.save(member_10)

member_11 = Gym_Member("Henry", "Higgins", 52, "27a Wimpole Street", "02083355326", "henry.higgins@btinternet.com", "True", "090", "True")
gym_member_repository.save(member_11)

member_12 = Gym_Member("Oliver", "Twist", 8, "Saffron Hill", "02082915201", "oliver.twiste@zoho.com", "False", "040", "False")
gym_member_repository.save(member_12)

member_13 = Gym_Member("Lemuel", "Gulliver", 29, "Fetter Lane, Old Jewry and Wapping", "02084725290", "lemuel.gulliver@aol.com", "False", "020", "False")
gym_member_repository.save(member_13)
 
member_14 = Gym_Member("Sweeney", "Todd", 31, "186 Fleet Street",  "02035339625", "sweeney.todd@outlook.com",  "False", "015", "False")
gym_member_repository.save(member_14)

member_15 = Gym_Member("Peter", "Pan", 13, "31 Kensington Park Gardens", "02085395519", "peter.pan@mail.com",  "False", "013", "True")
gym_member_repository.save(member_15)
 
member_16 = Gym_Member("George", "Smiley", 64, "9 Bywater Street, Chelsea", "02088687708", "george.smiley@outlook.com", "True", "006", "True")
gym_member_repository.save(member_16)

member_17 = Gym_Member("Winston", "Smith", 37, "27b Canonbury Square", "02033004574", "winston.smith@hotmail.com",  "False", "1984", "False")
gym_member_repository.save(member_17)

member_18 = Gym_Member("Mrs Anita", "Dearly", 24, "Outer Circle, The Regent's Park", "02034775638", "anita.dearly@hotmail.com", "True", "101", "True")
gym_member_repository.save(member_18)

member_19 = Gym_Member("Adolf", "Verloc", 46, "32 Brett Street, Soho", "02035878165", "adolf.verloc@zoho.com",  "False", "150", "False")
gym_member_repository.save(member_19)

member_20 = Gym_Member("Lady Marjorie", " Bellamy", 33, "165 Eaton Place", "02037768743", "marjorie.bellamy@aol.com", "True", "165", "True")
gym_member_repository.save(member_20)


#Class - Populate Class Table
class_1 = Gym_Class("Yoga", "45 minutes", 20, "Low", "Moderate", "25/03/2021", "09:15", "Sky Blue Studio")
gym_class_repository.save(class_1)

class_2 = Gym_Class("Pilates", "60 minutes", 25, "Low", "Easy", "24/03/2021", "15:30", "Sunshine Yellow Studio")
gym_class_repository.save(class_2)

class_3 = Gym_Class("Circuit Class", "30 minutes", 30,  "Moderate", "Hard", "30/03/2021", "10:30", "Meadow Green Studio")
gym_class_repository.save(class_3)

class_4 = Gym_Class("Zumba", "60 minutes", 30,  "Moderate", "Easy", "31/03/2021", "12:00", "Sunshine Yellow Studio")
gym_class_repository.save(class_4)

class_5 = Gym_Class("Cycle Class", "45 minutes", 20,  "High", "Moderate", "25/03/2021", "16:00", "Red Robin Studio")
gym_class_repository.save(class_5) 

class_6 = Gym_Class("Aerobics", "60 minutes", 30,  "Moderate", "Easy", "26/03/2021", "17:30", "Sky Blue Studio")
gym_class_repository.save(class_6)

class_7 = Gym_Class("Legs Bums and Tums", "45 minutes", 15,  "Moderate", "Moderate", "29/03/2021", "11:30", "Meadow Green Studio")
gym_class_repository.save(class_7)

class_8 = Gym_Class("HIIT", "30 minutes", 25,  "High", "Moderate", "27/03/2021", "11:30", "Red Robin Studio")
gym_class_repository.save(class_8)

class_9 = Gym_Class("Military Fitness", "60 minutes", 15,  "High", "Hard", "28/03/2021", "10:00", "Meadow Green Studio")
gym_class_repository.save(class_9)

class_10 = Gym_Class("Box Fit", "45 minutes", 10,  "Moderate", "Easy", "24/03/2021", "17:00", "Red Robin Studio")
gym_class_repository.save(class_10)


#CATEGORY - Populate Category Table
category_1 = Gym_Category("Flex and Core")
gym_category_repository.save(category_1)

category_2 = Gym_Category("Cardio")
gym_category_repository.save(category_2)

category_3 = Gym_Category("Strength Training")
gym_category_repository.save(category_3)

category_4 = Gym_Category("Strength and Tone")
gym_category_repository.save(category_4)


#BOOKINGS - Populate Booking Table
booking_1 = Gym_Booking("James Bond", "Yoga", "Flex and Core", 7, 20)
gym_booking_repository.save(booking_1)

booking_2 = Gym_Booking("sherlock Holmes", "Military Fitness", "Strength Training", 9, 25)
gym_booking_repository.save(booking_2)

booking_3 = Gym_Booking("Bridget Jones", "Legs Bums and Tums", "Strength and Tone", 24, 30)
gym_booking_repository.save(booking_3)

booking_4 = Gym_Booking("Hercule Poirot", "Box Fit", "Strength Training", 12, 30)
gym_booking_repository.save(booking_4)

booking_5 = Gym_Booking("Mary Poppins", "Pilates", "Flex and Core", 18, 20)
gym_booking_repository.save(booking_5)

booking_6 = Gym_Booking("Count Dracula", "Circuit Class", "Cardio", 25, 30)
gym_booking_repository.save(booking_6)

booking_7 = Gym_Booking("Great Uncle Bulgaria Womble", "Zumba", "Cardio", 3, 15)
gym_booking_repository.save(booking_7)

booking_8 = Gym_Booking("Paddington Bear", "Aerobics", "Flex and Core", 9, 25)
gym_booking_repository.save(booking_8)

booking_9 = Gym_Booking("Dr Henry Jekyl", "Cycle Class", "Cardio", 2, 15)
gym_booking_repository.save(booking_9)

booking_10 = Gym_Booking("Phileas", "Fogg", "HIIT", "Cardio", 1, 2)
gym_booking_repository.save(booking_10)


pdb.set_trace()