from medical_body import MedicalBody
from connectionDB import mysql
import math

class AdmissionDoctor(MedicalBody):
    """docstring for AdmissionDoctor."""

    def __init__(self, id, name, table):
        super(AdmissionDoctor, self).__init__(id, name, table)
        MedicalBody.__init__(self, id, name, table)
        self.seriously_distribution = {
            'serious': 0.2,
            'less_serious': 0.7,
            'slight': 1
        }

    def update_state_2(self):
        if self.time_left == 0 and self.patient != None:
            self.waiting_patient.append({
                'patient':self.patient,
                'diagnosis': self.seriously_simulator(random.random())
            })
            self.waiting_patient_process.append(self.process)

    def state_capture(self, arg):
        pass

    def self_simulator(self, R1, R2):
        if R1<(1/2):
            return int(5+6*math.sqrt(R2))
        else:
            return int(17-6*math.sqrt(1-R2))

    def seriously_simulator(self, R):
        if R < self.seriously_distribution['serious']:
            return 'serious'
        if R < self.seriously_distribution['less_serious']:
            return 'less_serious'
        if R < self.seriously_distribution['slight'] < R:
            return 'slight'
