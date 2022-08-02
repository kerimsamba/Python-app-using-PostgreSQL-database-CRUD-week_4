from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.owner import Owner
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route('/owners')
def owners():
    owners = owner_repository.select_all()
    return render_template("/owners/index.html", owners=owners)

@owners_blueprint.route('/owners/<id>')
def show(id):
    owner = owner_repository.select(id)
    pets = pet_repository.select_all()
    return render_template("/owners/show.html", owner=owner, pets=pets)

@owners_blueprint.route("/owners/new", methods=["GET"])
def new_owner():
    return render_template("/owners/new.html")

@owners_blueprint.route("/owners", methods=["POST"])
def create_owner():
    first_name = request.form["first_name"]
    surname = request.form["surname"]
    telephone = request.form["telephone"]
    email = request.form["email"]
    status = "active"
    owner = Owner(first_name, surname, telephone, email, status)
    owner_repository.save(owner)
    return redirect("/pets")

@owners_blueprint.route("/owners/edit/<id>", methods=["GET"])
def edit(id):
    owner = owner_repository.select(id)
    return render_template("owners/edit.html", owner=owner)

@owners_blueprint.route("/owners/<id>", methods=["POST"])
def change_owner_details(id):
    first_name = request.form["first_name"]
    surname = request.form["surname"]
    telephone = request.form["telephone"]
    email = request.form["email"]
    status = request.form["status"]
    id = request.form["id"]
    owner = Owner(first_name, surname, telephone, email, status, id)
    owner_repository.change(owner)
    return redirect("/owners")















