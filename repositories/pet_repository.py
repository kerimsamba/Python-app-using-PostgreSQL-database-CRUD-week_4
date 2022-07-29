from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def save(pet, vet_id, owner_id ):
    sql = "INSERT INTO pets(name, dob, type, treatment_notes, vet_id, owner_id) VALUES ( %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.dob, pet.type, pet.treatment_notes, vet_id, owner_id]
    results = run_sql( sql, values )
    pet.id =  results[0]['id']
    return pet

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        pet = Pet(pet['name'], pet['dob'], pet['type'], pet['treatment_notes'], pet['vet_id'], pet['owner_id'], pet['id'])
    return pet


