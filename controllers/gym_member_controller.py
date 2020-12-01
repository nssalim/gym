from flask import Blueprint, Flask, redirect, render_template, request

from models.gym_member import Gym_member
import repositories.gym_member_repository as gym_member_repository

gym_members_blueprint = Blueprint("gym_member", __name__)

# INDEX
@gym_members_blueprint.route("/gym_member")
def gym_member():
    gym_members = gym_member_repository.select_all()
    return render_template("gym_members/index.html", gym_members=gym_members)


# NEW
@gym_members_blueprint.route("/gym_member/new")
def new_gym_member():
    return render_template("gym_member/new.html")


# CREATE
@gym_members_blueprint.route("/gym_members", methods=["POST"])
def create_gym_member():
    details = request.form["details"]
    new_gym_member = Gym_Member(first_name, last_name, age, phone_number, email)
    gym_member_repository.save(new_gym_member)
    return redirect("/gym_members")


# EDIT
@gym_members_blueprint.route("/gym_members/<id>/edit")
def edit_gym_member(id):
    gym_member = gym_member_repository.select(id)
    return render_template('gym_members/edit.html', gym_member=gym_member)


# UPDATE
@gym_members_blueprint.route("/gym_members/<id>", methods=["POST"])
def update_gym_member(id):
    details = request.form["details"]
    gym_member = Gym_Member(first_name, last_name, age, phone_number, email, id)
    gym_member_repository.update(gym_member)
    return redirect("/gym_members")


# DELETE
@gym_members_blueprint.route("/gym_members/<id>/delete", methods=["POST"])
def delete_gym_member(id):
    gym_member_repository.delete(id)
    return redirect("/gym_members")
