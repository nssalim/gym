from db.run_sql import run_sql
from models.gym_booking import Gym_Booking

from models.gym_member import Gym_Member
import repositories.gym_member_repository as gym_member_repository

from models.gym_class import Gym_Class
import repositories.gym_class_repository as gym_class_repository

def save(gym_booking):
    sql = "INSERT INTO gym_bookings (gym_member_id, gym_class_id) VALUES (%s, %s) RETURNING id"
    values = [gym_booking.gym_member.id, gym_booking.gym_class.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_booking.id = id


def select_all():
    gym_bookings = []
    sql = "SELECT * FROM gym_bookings"
    results = run_sql(sql)
    for result in results:
        gym_member = gym_member_repository.select(result["gym_member_id"])
        gym_class = gym_class_repository.select(result["gym_class_id"])
        gym_booking = Gym_Booking(gym_member, gym_class, result["id"])
        gym_bookings.append(gym_booking)
    return gym_bookings


def select(id):
    sql = "SELECT * FROM gym_bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    gym_member = gym_member_repository.select(result["gym_member_id"])
    gym_class = gym_class_repository.select(result["gym_class_id"])
    gym_booking = Gym_Booking(gym_member, gym_class, result["id"])
    return gym_booking


def delete_all():
    sql = "DELETE FROM gym_bookings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM gym_bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(biting):
    sql = "UPDATE gym_bookings SET (gym_member_id, gym_class_id) = (%s, %s) WHERE id = %s"
    values = [gym_booking.gym_member.id, gym_booking.gym_class.id, gym_booking.id]
    run_sql(sql, values)
