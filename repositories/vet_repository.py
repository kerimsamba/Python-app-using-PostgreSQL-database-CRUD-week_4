from db.run_sql import run_sql
from models.vet import Vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def save(vet):
    sql = "INSERT INTO vets(first_name, surname) VALUES ( %s, %s ) RETURNING id"
    values = [vet.first_name, vet.surname]
    results = run_sql( sql, values )
    vet.id = results[0]['id']
    return vet

def select(id):
    vet = None
    sql = "SELECT * from vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        vet = Vet(result['first_name'], result['surname'], result['id'])
    return vet









