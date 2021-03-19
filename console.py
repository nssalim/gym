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


member_1 = Gym_Member("James", "Bond", 36, "30 Wellington Square, Chelsea", "02038805903", "james.bond@zoho.com", "premium", "007", "is_active")
gym_member_repository.save(member_1)

member_2 = Gym_Member("sherlock", "Holmes", 40, "221b Baker Street","02087047780", "sherlock.holmes@outlook.com", "premium", "221", "is_active")
gym_member_repository.save(member_2)

member_3 = Gym_Member("Bridget", "Jones", 26, "8 Bedale Street", "02038696256", "bridget.jones@mail.com", "premium", "003", "is_active")
gym_member_repository.save(member_3)

member_4 = Gym_Member("Hercule", "Poirot",  58, "56B Whitehavens Mansions",  "02083473422", "hercule.poirot@aol.com", "premium", "300", "is_active")
gym_member_repository.save(member_4)

member_5 = Gym_Member("Mary", "Poppins", 29, "17 Cherry Tree Lane", "02084972723", "mary.poppins@gmail.com", "premium", "004", "is_active")
gym_member_repository.save(member_5)

member_6 = Gym_Member("Count", "Dracula", 121, "Eon House, 138 Piccadilly",  "02037444469",  "count.dracula@mail.com", "premium", "666", "is_active")
gym_member_repository.save(member_6)

member_7 = Gym_Member("Great Uncle Bulgaria", "Womble",  63, "6 Wimbledon Common", "02088361453", "greatunclebulgaria.womble@hotmail.com", "premium", "100", "is_active")
gym_member_repository.save(member_7)

member_8 = Gym_Member("Paddington", "Bear", 12, "32 Windsor Gardens",  "02033150554", "paddington.bear@yahoo.com", "premium", "400", "is_active")
gym_member_repository.save(member_8)

member_9 = Gym_Member("Dr Henry", "Jekyl", 44, "28 Leicester Square", "02031892862", "henry.jekyl@gmail.com", "premium", "002", "is_active")
gym_member_repository.save(member_9)
 
member_10 = Gym_Member("Phileas", "Fogg", 31, "7 Savile Row, Burlington Gardens",  "02086187613", "phileas.fogg@btinternet.com", "premium", "080", "is_active")
gym_member_repository.save(member_10)

member_11 = Gym_Member("Henry", "Higgins", 52, "27a Wimpole Street", "02083355326", "henry.higgins@btinternet.com", "premium", "090", "is_active")
gym_member_repository.save(member_11)

member_12 = Gym_Member("Oliver", "Twist", 8, "Saffron Hill", "02082915201", "oliver.twiste@zoho.com", "premium", "040", "is_active")
gym_member_repository.save(member_12)

member_13 = Gym_Member("Lemuel", "Gulliver", 29, "Fetter Lane, Old Jewry and Wapping", "02084725290", "lemuel.gulliver@aol.com", "premium", "020", "is_active")
gym_member_repository.save(member_13)
 
member_14 = Gym_Member("Sweeney", "Todd", 31, "186 Fleet Street",  "02035339625", "sweeney.todd@outlook.com",  "premium", "015", "is_active")
gym_member_repository.save(member_14)

member_15 = Gym_Member("Peter", "Pan", 13, "31 Kensington Park Gardens", "02085395519", "peter.pan@mail.com",  "premium", "013", "is_active")
gym_member_repository.save(member_15)
 
member_16 = Gym_Member("George", "Smiley", 64, "9 Bywater Street, Chelsea", "02088687708", "george.smiley@outlook.com", "premium", "006", "is_active")
gym_member_repository.save(member_16)

member_17 = Gym_Member("Winston", "Smith", 37, "27b Canonbury Square", "02033004574", "winston.smith@hotmail.com",  "premium", "1984", "is_active")
gym_member_repository.save(member_17)

member_18 = Gym_Member("Mrs Anita", "Dearly", 24, "Outer Circle, The Regent's Park", "02034775638", "anita.dearly@hotmail.com", "premium", "101", "is_active")
gym_member_repository.save(member_18)

member_19 = Gym_Member("Adolf", "Verloc", 46, "32 Brett Street, Soho", "02035878165", "adolf.verloc@zoho.com",  "premium", "150", "is_active")
gym_member_repository.save(member_19)

member_20 = Gym_Member("Lady Marjorie", " Bellamy", 33, "165 Eaton Place", "02037768743", "marjorie.bellamy@aol.com", "premium", "165", "is_active")
gym_member_repository.save(member_20)

class_1 = Gym_Class("yoga", 15)
gym_class_repository.save(class_1)

class_2 = Gym_Class("pilates", 25)
gym_class_repository.save(class_2)

class_3 = Gym_Class("circuit class", 30)
gym_class_repository.save(class_3)

class_4 = Gym_Class("zumba", 20)
gym_class_repository.save(class_4)

class_5 = Gym_Class("cycle class", 30)
gym_class_repository.save(class_5) 

class_6 = Gym_Class("aerobics", 22)
gym_class_repository.save(class_6)

class_7 = Gym_Class("box fit", 28)
gym_class_repository.save(class_7)

category_1 = Gym_Category("Conditioning")
gym_category_repository.save(category_1)


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