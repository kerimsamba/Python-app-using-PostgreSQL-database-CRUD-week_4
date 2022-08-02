from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.appointment import Appointment
import repositories.appointment_repository as appointment_repository
import repositories.pet_repository as pet_repository

appointments_blueprint = Blueprint("appointment", __name__)

@appointments_blueprint.route('/appointments')
def appointments():
    appointments = appointment_repository.select_all()
    return render_template("/appointment/index.html", appointments=appointments)

@appointments_blueprint.route('/appointments/<id>')
def show(id):
    appointment = appointment_repository.select(id)
    pets = pet_repository.select_all()
    return render_template("/appointments/show.html", appointment=appointment, pets=pets)

@appointments_blueprint.route("/appointments/new", methods=["GET"])
def new_appointment():
    return render_template("/appointments/new.html")