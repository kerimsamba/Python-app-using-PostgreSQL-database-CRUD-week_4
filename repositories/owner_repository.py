from db.run_sql import run_sql
from models.owner import Owner

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def save(owner):
    sql = "INSERT INTO owners(first_name, surname, telephone, email, status) VALUES ( %s, %s, %s, %s, %s) RETURNING id"
    values = [owner.first_name, owner.surname, owner.telephone, owner.email, owner.status]
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
        owner = Owner(result['first_name'], result['surname'], result['telephone'], result['email'], result['status'], result['id'])
    return owner

def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['first_name'], row['surname'], row['telephone'], row['email'], row['status'], row['id'])
        owners.append(owner)
    return owners

def change(owner):
    sql = "UPDATE owners SET first_name = %s, surname = %s, telephone = %s, email = %s, status = %s WHERE id = %s;"
    values = [owner.first_name, owner.surname, owner.telephone, owner.email, owner.status, owner.id]
    run_sql( sql, values)

