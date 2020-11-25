from medical_body import MedicalBody
from connectionDB import mysql
import random

class EmergencyDoctor(MedicalBody):
    """docstring for AdmissionDoctor."""

    def __init__(self, id, name):
        super(EmergencyDoctor, self).__init__()
        MedicalBody.__init__(self, id, name)
        self.room_distribution = {
            'x-ray': 0.6,
            'nurse': 1
        }

    def assign_patient(self, patient, allotted_time, random_time, process):
        self.allotted_time = allotted_time
        self.time_left = self.allotted_time
        self.random_time = random_time
        self.process = process
        self.patient = patient
        self_busy = True

    def state_capture(self, arg):
        pass

    def self_simulator(self):
        random_sum = 0
        minutes = 0
        for i in range(12):
            while True:
            random_sum += random.random()
            minutes = 10+8*(random_sum-6)
            if minutes > 0
                break
        return int(minutes)

    def room_simulator(self, R):
        if R < self.room_distribution['x-ray']:
            return 'x-ray'
        if R < self.room_distribution['nurse']:
            return 'nurse'
