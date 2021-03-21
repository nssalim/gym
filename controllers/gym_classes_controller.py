from flask import Flask, Blueprint, redirect, render_template, request

from models.gym_class import Gym_Class
import repositories.gym_class_repository as gym_class_repository

import repositories.gym_member_repository as gym_member_repository
import repositories.gym_booking_repository as gym_booking_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

# INDEX
@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", gym_classes=gym_classes)

# NEW
@gym_classes_blueprint.route("/gym_classes/new", methods=["GET"])
def new_gym_class():
    return render_template("gym_classes/new.html")


# CREATE
@gym_classes_blueprint.route("/gym_classes", methods=["POST"])
def create_gym_class():
    name = request.form["gym_class-name"]
    gym_class = gym_class(name)
    gym_class_repository.save(gym_class)
    return redirect("/gym_classes")

# EDIT
@gym_classes_blueprint.route("/gym_classes/<id>/edit")
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    gym_member = gym_member_repository.select_all()
    return render_template('gym_classes/edit.html', gym_class=gym_class, gym_members=gym_members)


# DELETE
@gym_classes_blueprint.route("/gym_classes/<id>/delete", methods=["POST"])
def delete_gym_class(id):
    gym_class_repository.delete(id)
    return redirect("/gym_classes")

# DISPLAY 
@gym_classes_blueprint.route("/gym_classes/<id>")
def show_gym_class(id):
    attending_members = gym_class_repository.select_occupancy_of_gym_class(id)
    gym_class = gym_class_repository.select(id)
    return render_template("gym_classes/show.html", attending_members=attending_members, gym_class=gym_class)


