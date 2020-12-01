from connectionDB import mysql, create_entities

class Patient(object):
    """docstring for Patient."""

    def __init__(self, id, name):
        super(Patient, self).__init__()
        self.id = id
        self.name = name
        self.random_time = 0
        self.admission_minute = 0
        self.departure_minute = 0
        self.finished = False
        self.final_time = 0
        self.severity = None

    def update_state(self):
        self.final_time += 1

    def state_capture(self):
        cnx = mysql()
        cursor = cnx.cursor()

        update = 'UPDATE pacientes SET (tiempoTotal = %s, finalizado = %s) WHERE id = %s'
        cursor.execute(update, (self.final_time, self.finished, self.id))

        cnx.commit()
        cursor.close()
        cnx.close()
