from db.run_sql import run_sql
from models.appointment import Appointment

def save(appointment):
    sql = "INSERT INTO appointments(pet_id, check_in, check_out) VALUES ( %s, %s, %s) RETURNING id"
    values = [appointment.pet_id, appointment.check_in, appointment.check_out]
    results = run_sql( sql, values)
    appointment.id = results[0]['id']
    return appointment

def delete(id):
    sql = "DELETE * from appointments WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

def select_all():
    appointments = []

    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    for row in results:
        appointment = Appointment(row['pet_id'], row["check_in"], row["check_out"], row['id'])
        appointments.append(appointment)
    return appointments