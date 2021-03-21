from db.run_sql import run_sql

from models.gym_member import Gym_Member

from models.gym_class import Gym_Class
import repositories.gym_class_repository as gym_class_repository

from models.gym_category import Gym_Category
import repositories.gym_category_repository as gym_category_repository

from models.gym_booking import Gym_Booking
import repositories.gym_booking_repository as gym_booking_repository

# SAVE
def save(gym_member):
    sql = "INSERT INTO gym_members (first_name, last_name, age, address, phone_no, email, premium, membership_no, is_active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [gym_member.first_name, gym_member.last_name, gym_member.age, gym_member.address, gym_member.phone_no, gym_member.email, gym_member.premium, gym_member.membership_no, gym_member.is_active,]
    results = run_sql(sql, values)
    gym_member.id = results[0]['id']
    return gym_member

# SELECT ALL
def select_all():
    gym_members = []
    sql = "SELECT * FROM gym_members ORDER BY last_name"
    results = run_sql(sql)
    for result in results:
        gym_member = Gym_Member(result["first_name"], result["last_name"], result["age"], result["address"], result["phone_no"], result["email"], result["premium"], result["membership_no"], result["is_active"], result["id"])
        gym_members.append(gym_member)
    return gym_members

# SELECT ONE
def select(id):
    gym_member = None
    sql = "SELECT * FROM gym_members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        gym_member = Gym_Member(result["first_name"], result["last_name"], result["age"], result["address"], result["phone_no"], result["email"], result["premium"], result["membership_no"], result["is_active"], result["id"])
    return gym_member

# DELETE ALL
def delete_all():
    sql = "DELETE FROM gym_members"
    run_sql(sql)

# DELETE ONE
def delete(id):
    sql = "DELETE FROM gym_members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE
def update(gym_member):
    sql = "UPDATE gym_members SET (first_name, last_name, age, address, phone_no, email, premium, membership_no, is_active) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [gym_member.first_name, gym_member.last_name, gym_member.age, gym_member.address, gym_member.phone_no, gym_member.email, gym_member.premium, gym_member.membership_no, gym_member.is_active]
    run_sql(sql, values)

# DISPLAY GYM BOOKINGS BY MEMBER  
def gym_bookings_by_member(gym_member):
    gym_bookings = []
    sql = "SELECT * FROM gym_bookings WHERE gym_member_id = %s"
    values = [gym_member.id]
    results = run_sql(sql, values)
    for result in results:
        gym_class = gym_class_repository.select(result["gym_class_id"])
        gym_category = gym_category_repository.select(result["gym_category_id"])
        gym_booking = Gym_Booking(gym_member, gym_class, gym_category, result["bookings"], result["booked_count"], result["id"])
        gym_bookings.append(gym_booking)
    return gym_bookings