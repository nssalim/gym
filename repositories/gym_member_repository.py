from db.run_sql import run_sql
from models.gym_member import Gym_Member

def save(gym_member):
    sql = "INSERT INTO gym_members (first_name, last_name, age, phone_number, email) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [gym_member.first_name, gym_member.last_name, gym_member.age, gym_member.phone_number, gym_member.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_member.id = id


def select_all():
    gym_members = []
    sql = "SELECT * FROM gym_members"
    results = run_sql(sql)
    for result in results:
        gym_member = Gym_Member(result["details"], result["id"])
        gym_members.append(gym_member)
    return gym_members


def select(id):
    sql = "SELECT * FROM gym_members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    gym_member = Gym_Member(result["details"], result["id"])
    return gym_member


def delete_all():
    sql = "DELETE FROM gym_members"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM gym_members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(gym_member):
    sql = "UPDATE gym_members SET details = %s WHERE id = %s"
    values = [gym_member.first_name, gym_member.last_name, gym_member.age, gym_member.phone_number, gym_member.email, gym_member.id]
    run_sql(sql, values)
