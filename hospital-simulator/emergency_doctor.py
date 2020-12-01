from medical_body import MedicalBody
from connectionDB import mysql
import random

class EmergencyDoctor(MedicalBody):
    """docstring for AdmissionDoctor."""

    def __init__(self, id, name, table=''):
        super(EmergencyDoctor, self).__init__()
        MedicalBody.__init__(self, id, name, 'doctores_urgencias')
        self.room_distribution = {
            'x-ray': 0.6,
            'nurse': 1
        }
    def update_state_2(self):
        if self.time_left == 0 and self.patient != None:
            self.waiting_patient.append({
                'patient':self.patient,
                'diagnosis': self.room_simulator(random.random()),
                'process': self.process
            })

    def state_capture(self, arg):
        pass

    def self_simulator(self):
        random_sum = 0
        minutes = 0
        while True:
            random_sum = 0
            minutes = 0
            for i in range(12):
                random_sum += random.random()
            minutes = 10+8*(random_sum-6)
            if minutes > 0:
                break
        return int(minutes), random_sum

    def room_simulator(self, R):
        if R < self.room_distribution['x-ray']:
            return 'x-ray'
        if R < self.room_distribution['nurse']:
            return 'nurse'
