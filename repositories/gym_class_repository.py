from db.run_sql import run_sql
from models.gym_class import Gym_Class
from models.gym_booking import Gym_Booking

from models.gym_member import Gym_Member
import repositories.gym_member_repository as gym_member_repository


def save(gym_class):
    sql = "INSERT INTO gym_classes (name, capacity) VALUES (%s, %s) RETURNING id"
    values = [gym_class.name, gym_class.capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_class.id = id


def select_all():
    gym_classes = []
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    for result in results:
        gym_member = gym_member_repository.select(result["gym_member_id"])
        gym_class = Gym_Class(result["details"], gym_member, result["id"])
        gym_classes.append(gym_class)
    return gym_classes


def select(id):
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    gym_member = gym_member_repository.select(result["gym_member_id"])
    gym_class = Gym_Class(result["details"], gym_member, result["id"])
    return gym_class


def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# To fix later
def update(gym_class):
    sql = "UPDATE gym_classes SET (name, capacity, fill_up_occupancy, size_of_class, gym_class_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.name, gym_class.capacity, gym_class.fill_up_occupancy, gym_class.size_of_class, gym_class.id]
    run_sql(sql, values)


def select_occupancy_of_gym_class(id):
    attending_members = []
    sql = "SELECT gym_members.* FROM gym_members INNER JOIN gym_bookings ON bookings.gym_member_id = gym_members.id WHERE gym_bookings.gym_class_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        gym_member = Gym_Member(result["details"])
        attending_members.append(gym_member)
    return attending_members    