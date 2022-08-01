from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("/pets/index.html", pets = pets)

@pets_blueprint.route("/pets/<id>")
def show(id):
    pet = pet_repository.select(id)
    vet = vet_repository.select(pet.vet_id)
    owner = owner_repository.select(pet.owner_id)
    vets = vet_repository.select_all()
    return render_template("pets/show.html", pet=pet, vet=vet, owner=owner)

@pets_blueprint.route("/pets/new")
def new_pet():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("pets/new.html", owners=owners, vets=vets )

@pets_blueprint.route("/pets", methods=["POST"])
def create_pet():
    name = request.form["name"]
    dob = request.form["dob"]
    type = request.form["type"]
    treatment_notes = request.form["treatment_notes"]
    vet_id = request.form["vet_id"]
    owner_id = request.form["owner_id"]
    pet = Pet(name, dob, type, treatment_notes, vet_id, owner_id)
    pet_repository.save(pet)
    return redirect("/pets")
    


