from connectionDB import mysql, create_entities

class XRay(object):
    """docstring for XRay."""

    def __init__(self, id):
        super(XRay, self).__init__()
        self.id = id
        self.busy = False
        self.patient = None
        self.time_left = 0
        self.allotted_time = 0
        self.random_time = 0
        self.waiting_patient = []
        create_entities('radiografia', self.id )

    def assign_patient(self,  patient, allotted_time, random_time):
        self.allotted_time = allotted_time
        self.time_left = self.allotted_time
        self.random_time = random_time
        self.patient = patient
        self_busy = True

    def update_state(self):
        if self.busy:
            self.time_left -= 1
            self.patient.update_state()
            if self.time_left == 0:
                self.busy = False
                self.allotted_time = 0
                self.random_time = 0
                self.process = None
                self.diagnosis = None
        for patient in self.waiting_patient:
            patient.update_state()
        if self.time_left == 0 and self.patient != None:
            self.waiting_patient.append(self.patient)
            self.patient = None

    def next_waiting_patient(self):
        patient = self.waiting_patient.pop(0)
        return patient

    def self_simulator(self, R):
        return int(10+10*R)

    def state_capture(self):
        pass
