from db.run_sql import run_sql

from models.gym_booking import Gym_Booking

from models.gym_member import Gym_Member
import repositories.gym_member_repository as gym_member_repository

from models.gym_class import Gym_Class
import repositories.gym_class_repository as gym_class_repository

from models.gym_category import Gym_Category
import repositories.gym_category_repository as gym_category_repository

# SAVE
def save(gym_booking):
    sql = "INSERT INTO gym_bookings (gym_member_id, gym_class_id, gym_category_id, bookings, booked_count) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [gym_booking.gym_member_id, gym_booking.gym_class_id, gym_booking.gym_category_id, gym_booking.bookings, gym_booking.booked_count]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_booking.id = id
    return gym_booking

# SELECT ALL
def select_all():
    gym_bookings = []
    sql = "SELECT * FROM gym_bookings ORDER BY gym_member_id ASC, booked_count DESC"
    results = run_sql(sql)
    for result in results:
        gym_member = gym_member_repository.select(result["gym_member_id"])
        gym_class = gym_class_repository.select(result["gym_class_id"])
        gym_category = gym_category_repository.select(result["gym_category_id"])
        gym_booking = Gym_Booking(gym_member, gym_class, gym_category, result["bookings"], result["booked_count"], result["id"])
        gym_bookings.append(gym_booking)
    return gym_bookings

# SELECT ONE
def select(id):
    gym_booking = None
    sql = "SELECT * FROM gym_bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        gym_member = gym_member_repository.select(result["gym_member_id"])
        gym_class = gym_class_repository.select(result["gym_class_id"])
        gym_category = gym_category_repository.select(result["gym_category_id"])
        gym_booking = Gym_Booking(gym_member, gym_class, gym_category, result["bookings"], result["booked_count"], result["id"])
    return gym_booking

# DELETE ALL
def delete_all():
    sql = "DELETE FROM gym_bookings"
    run_sql(sql)

# DELETE ONE
def delete(id):
    sql = "DELETE FROM gym_bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE
def update(gym_booking):
    sql = "UPDATE gym_bookings SET (gym_member_id, gym_class_id, gym_category_id, bookings, booked_count) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [gym_booking.gym_member.id, gym_booking.gym_class.id, gym_booking.gym_category_id, gym_booking.bookings, gym_booking.booked_count]
    run_sql(sql, values)

# ADD BOOKING
def add_booking(id):
    sql = "UPDATE gym_bookings SET bookings = bookings +1 WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELETE BOOKING
def delete_booking(id):
    sql = "UPDATE gym_bookings SET bookings = bookings -1, booked_count = booked_count +1 WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DISPLAY GYM BOOKINGS BY POPULARITY
def popular():
    gym_bookings = []
    sql = "SELECT * FROM gym_bookings ORDER BY booked_count DESC LIMIT 10"
    results = run_sql(sql)
    for result in results:
        gym_member = gym_member_repository.select(result["gym_member_id"])
        gym_class = gym_class_repository.select(result["gym_class_id"])
        gym_category = gym_category_repository.select(result["gym_category_id"])
        gym_booking = Gym_Booking(gym_member, gym_class, gym_category, result["bookings"], result["booked_count"], result["id"])
        gym_bookings.append(gym_booking)
    return gym_bookings
