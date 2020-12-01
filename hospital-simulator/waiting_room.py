from connectionDB import mysql, create_entities

class WaitingRoom(object):
    """docstring for WaitingRoom."""

    def __init__(self, id):
        super(WaitingRoom, self).__init__()
        self.id = id
        self.patients = []
        create_entities('hospital_ingreso', self.id)


    def assign_patient(self, patient):
        self.patients.append(patient)

    def removePatient(self):
        self.patients.pop(0)

    def update_state(self):
        for patient in self.patients:
            patient.update_state()

    def state_capture(self, arg):
        pass
