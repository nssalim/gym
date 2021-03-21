from flask import Flask, Blueprint, render_template, request, redirect

from models.gym_category import Gym_Category
import repositories.gym_category_repository as gym_category_repository

gym_categories_blueprint = Blueprint("gym_categories", __name__)

# DISPLAYS LIST OF GYM CATEGORIES 
@gym_categories_blueprint.route("/gym_categories")
def gym_categories():
    gym_categories = gym_category_repository.select_all()
    return render_template("gym_categories/index.html", gym_categories = gym_categories)

# ADD NEW GYM CATEGORY TO DATABASE
@gym_categories_blueprint.route("/gym_categories/new", methods=['GET'])
def new_gym_category():
    return render_template("gym_categories/new.html")

# ADD NEW GYM CATEGORY AND UPDATE LIST
@gym_categories_blueprint.route("/gym_categories", methods=['POST'])
def create_gym_category():
    category = request.form['gym_category-category']
    gym_category = Gym_category(category)
    gym_category_repository.save(gym_category)
    return redirect("/gym_categories")

# ALL GYM BOOKINGS BY A SPECIFIC GYM CATEGORY
@gym_categories_blueprint.route("/gym_categories/<id>")
def gym_category_gym_bookings(id):
    gym_category = gym_category_repository.select(id)
    gym_categories_gym_bookings = gym_category_repository.gym_bookings_by_gym_category(gym_category)
    return render_template("gym_categories/show.html", gym_category = gym_category, gym_bookings = gym_categories_gym_bookings)