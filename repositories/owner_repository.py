from db.run_sql import run_sql
from models.owner import Owner

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def save(owner):
    sql = "INSERT INTO owners(first_name, surname) VALUES ( %s, %s ) RETURNING id"
    values = [owner.first_name, owner.surname]
    results = run_sql( sql, values)
    owner.id = results[0]['id']
    return owner

def select(id):
    owner = None
    sql = "SELECT * from owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        owner = Owner(result['first_name'], result['surname'], result['id'])
    return owner


