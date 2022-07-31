from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.owner import Owner
import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint("owners", __name__)