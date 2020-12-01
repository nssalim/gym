from flask import Blueprint, Flask, redirect, render_template, request

from models.gym_class import Gym_Class
import repositories.gym_class_repository as gym_class_repository
import repositories.gym_member_repository as gym_member_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

# INDEX
@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", gym_classes=gym_classes)


# SHOW
@gym_classes_blueprint.route("/gym_classes/<id>")
def show_gym_class(id):
    attending_members = gym_class_repository.select_occupancy_of_gym_class(id)
    gym_class = gym_class_repository.select(id)
    return render_template("gym_classes/show.html", attending_members=attending_members, gym_class=gym_class)


# NEW
@gym_classes_blueprint.route("/gym_classes/new")
def new_gym_class():
    gym_members = gym_member_repository.select_all()
    return render_template("gym_classes/new.html", gym_members=gym_members)


# CREATE
@gym_classes_blueprint.route("/gym_classes", methods=["POST"])
def create_gym_class():
    details = request.form["details"]
    gym_member_id = request.form["gym_member_id"]
    gym_member = gym_member_repository.select(gym_member_id)
    new_gym_class = Gym_Class(name, capacity, fill_up_occupancy, size_of_class)
    gym_class_repository.save(new_gym_class)
    return redirect("/gym_classes")


# EDIT
@gym_classes_blueprint.route("/gym_classes/<id>/edit")
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    gym_member = gym_member_repository.select_all()
    return render_template('gym_classes/edit.html', gym_class=gym_class, gym_members=gym_members)


# UPDATE
@gym_classes_blueprint.route("/gym_classes/<id>", methods=["POST"])
def update_gym_class(id):
    details = request.form["details"]
    gym_member_id = request.form["gym_member_id"]
    gym_member = gym_member_repository.select(gym_member_id)
    gym_class = Gym_Class(name, capacity, fill_up_occupancy, size_of_class, id)
    gym_class_repository.update(gym_class)
    return redirect("/gym_classes")


# DELETE
@gym_classes_blueprint.route("/gym_classes/<id>/delete", methods=["POST"])
def delete_gym_class(id):
    gym_class_repository.delete(id)
    return redirect("/gym_classes")
