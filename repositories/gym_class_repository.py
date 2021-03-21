from db.run_sql import run_sql

from models.gym_class import Gym_Class

from models.gym_member import Gym_Member
import repositories.gym_member_repository as gym_member_repository

from models.gym_booking import Gym_Booking

import repositories.gym_category_repository as gym_category_repository

# SAVE 
def save(gym_class):
    sql = "INSERT INTO gym_classes (title, duration, capacity, intensity, difficulty, date, time, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [gym_class.title, gym_class.duration, gym_class.capacity, gym_class.intensity, gym_class.difficulty, gym_class.date, tgym_class.ime, gym_class.location ]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

# SELECT ALL
def select_all():
    gym_classes = []
    sql = "SELECT * FROM gym_classes by title"
    results = run_sql(sql)
    for result in results:
        gym_member = gym_class(result["title"], result["id"])
        gym_classes.append(gym_class)
    return gym_classes

# SELECT ONE
def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        gym_class = gym_class(result["title"], result["id"])
    return gym_class

# DELETE ALL
def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

# DELETE ONE
def delete(id):
    sql = "DELETE FROM gym_members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DISPLAY GYM BOOKINGS BY CLASS
def gym_bookings_by_gym_class(gym_class):
    gym_bookings = []
    sql = "SELECT * FROM gym_bookings WHERE gym_class_id = %s"
    values = [gym_class.id]
    results = run_sql(sql, values)
    for result in results:
        gym_member = gym_member_repository.select(result["gym_member_id"])
        gym_category= gym_category_repository.select(result["gym_category_id"])
        gym_booking = Gym_Booking(gym_member, gym_class, gym_category, result["bookings"], result["booked_count"], result["id"])
        gym_bookings.append(gym_booking)     
    return gym_bookings