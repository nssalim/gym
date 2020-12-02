from flask import Blueprint, Flask, redirect, render_template, request

from models.gym_booking import Gym_Booking
import repositories.gym_booking_repository as gym_booking_repository

import repositories.gym_member_repository as gym_member_repository
import repositories.gym_class_repository as gym_class_repository

gym_bookings_blueprint = Blueprint("gym_bookings", __name__)

# INDEX
@gym_bookings_blueprint.route("/gym_booking")
def gym_bookings():
    gym_bookings = gym_booking_repository.select_all()
    return render_template("gym_bookings/index.html", gym_bookings=gym_bookings)


# NEW
@gym_bookings_blueprint.route("/gym_bookings/new")
def new_gym_booking():
    gym_members = gym_member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_bookings/new.html", gym_members=gym_members, gym_classes=gym_classes)


# CREATE
@gym_bookings_blueprint.route("/gym_bookings", methods=["POST"])
def create_gym_booking():
    gym_member_id = request.form["gym_member_id"]
    gym_class_id = request.form["gym_class_id"]
    gym_member = gym_member_repository.select(gym_member_id)
    gym_class = gym_class_repository.select(gym_class_id)
    new_gym_booking = Gym_Booking(gym_member, gym_class)
    gym_booking_repository.save(new_gym_booking)
    return redirect("/gym_bookings")


# EDIT
@gym_bookings_blueprint.route("/gym_bookings/<id>/edit")
def edit_gym_booking(id):
    gym_booking = gym_booking_repository.select(id)
    gym_members = gym_member_repository.select_all()
    gym_class = gym_class_repository.select_all()
    return render_template('gym_bookings/edit.html', gym_booking=gym_booking, gym_members=gym_members, gym_classes=gym_classes)


# UPDATE
@gym_bookings_blueprint.route("/gym_bookings/<id>", methods=["POST"])
def update_gym_booking(id):
    gym_member_id = request.form["gym_member_id"]
    gym_class_id = request.form["gym_class_id"]
    gym_member = gym_member_repository.select(gym_member_id)
    gym_class = gym_class_repository.select(gym_class_id)
    gym_booking = Gym_Booking(gym_member, gym_class, id)
    gym_booking_repository.update(gym_booking)
    return redirect("/gym_bookings")


# DELETE
@gym_bookings_blueprint.route("/gym_bookings/<id>/delete", methods=["POST"])
def delete_gym_booking(id):
    gym_booking_repository.delete(id)
    return redirect("/gym_bookings")
