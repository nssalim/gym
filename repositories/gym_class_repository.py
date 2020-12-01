from db.run_sql import run_sql
from models.gym_member import Gym_Member
from models.gym_class import Gym_Class
from models.gym_booking import Gym_Booking






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