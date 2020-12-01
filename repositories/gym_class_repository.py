from db.run_sql import run_sql
from models.gym_member import Gym_Member
from models.gym_class import Gym_Class
from models.gym_booking import Gym_Booking
import repositories.zombie_type_repository as zombie_type_repository

def save(gym_booking):
    sql = "INSERT INTO gym_bookings (name, zombie_type_id) VALUES (%s, %s) RETURNING id"
    values = [zombie.name, zombie.zombie_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    zombie.id = id


def select_all():
    zombies = []
    sql = "SELECT * FROM zombies"
    results = run_sql(sql)
    for result in results:
        zombie_type = zombie_type_repository.select(result["zombie_type_id"])
        zombie = Zombie(result["name"], zombie_type, result["id"])
        zombies.append(zombie)
    return zombies


def select(id):
    sql = "SELECT * FROM zombies WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    zombie_type = zombie_type_repository.select(result["zombie_type_id"])
    zombie = Zombie(result["name"], zombie_type, result["id"])
    return zombie


def delete_all():
    sql = "DELETE FROM zombies"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM zombies WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(zombie):
    sql = "UPDATE zombies SET (name, zombie_type_id) = (%s, %s) WHERE id = %s"
    values = [zombie.name, zombie.zombie_type.id, zombie.id]
    run_sql(sql, values)


def select_victims_of_zombie(id):
    victims = []
    sql = "SELECT humans.* FROM humans INNER JOIN bitings ON bitings.human_id = humans.id WHERE bitings.zombie_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        human = Human(result["name"])
        victims.append(human)
    return victims








def delete_all():
    sql = "DELETE FROM gym_class"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM gym_class WHERE id = %s"
    values = [id]
    run_sql(sql, values)


    def select_number_of_bookings(id):
    bookings = []
    sql = "SELECT gym_members.* FROM gym_members INNER JOIN gym_bookings ON bookings.gym_member_id = gym_members.id WHERE gym_bookings.gym_class_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        gym_member = Gym_Member(result["name"])
        gym_bookings.append(gym_member)
    return gym_bookingss