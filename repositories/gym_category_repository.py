from db.run_sql import run_sql

from models.gym_category import Gym_Category

from models.gym_member import Gym_Member
import repositories.gym_member_repository as gym_member_repository

from models.gym_class import Gym_Class
import repositories.gym_class_repository as gym_class_repository

from models.gym_booking import Gym_Booking

# SAVE 
def save(gym_category):
    sql = "INSERT INTO gym_category (category) VALUES (%s) RETURNING id"
    values = [gym_category.category]
    results = run_sql(sql, values)
    gym_category.id = results[0]['id']
    return gym_category

# SELECT ALL
def select_all():
    gym_categories = []
    sql = "SELECT * FROM gym_categories ORDER BY category"
    results = run_sql(sql)
    for result in results:
        gym_category = Gym_Category(result["category"], result["id"])
        gym_categories.append(gym_category)
    return gym_categories

# SELECT ONE
def select(id):
    gym_category = None
    sql = "SELECT * FROM gym_categories WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        gym_category = Gym_category(result["category"], result["id"])
    return gym_category

# DELETE ALL
def delete_all():
    sql = "DELETE FROM gym_categories"
    run_sql(sql)

# DELETE ONE
def delete(id):
    sql = "DELETE FROM gym_categories WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DISPLAY GYM BOOKINGS BY CATEGORY
def bookings_by_gym_category(gym_category):
    gym_Bookings = []
    sql = "SELECT * FROM gym_bookings WHERE gym_category_id = %s"
    values = [gym_category.id]
    results = run_sql(sql,values)
    for result in results:
        gym_member = gym_member_repository.select(result['gym_member_id'])
        gym_class = gym_class_repository.select(result['gym_class_id'])
        gym_booking = Gym_Booking(gym_member, gym_class, gym_category, result["bookings"], result["booked_count"], result["id"])
        gym_bookings.append(gym_booking)
    return gym_bookings