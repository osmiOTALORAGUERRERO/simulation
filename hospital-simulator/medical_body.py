from connectionDB import mysql, create_entities

class MedicalBody(object):
    """docstring for MedicalBody."""

    def __init__(self, id, name, table):
        super(MedicalBody, self).__init__()
        self.id = id
        self.name = name
        self.busy = False
        self.patient = None
        self.time_left = 0
        self.allotted_time = 0
        self.random_time = 0
        self.process = None
        self.waiting_patient = []
        create_entities(table, self.id, self.name)

    def assign_patient(self, patient, allotted_time, random_time, process=None):
        self.allotted_time = allotted_time
        self.time_left = self.allotted_time
        self.random_time = random_time
        self.patient = patient
        self.process = process
        self.busy = True

    def update_state(self):
        updated = False
        if self.busy:
            self.time_left -= 1
            self.patient.update_state()
            if self.time_left == 0:
                self.busy = False
                self.allotted_time = 0
                self.random_time = 0
                self.process = None
            updated = True

        for patient in waiting_patient:
            patient.update_state()
        self.update_state_2()
        self.patient = None
        self.process = None
        return updated

    def update_state_2(self):
        if self.time_left == 0 and self.patient != None:
            self.waiting_patient.append(self.patient)

    def next_waiting_patient(self):
        patient = self.waiting_patient.pop(0)
        return patient
