from medical_body import MedicalBody
from connectionDB import mysql
from math

class AdmissionDoctor(MedicalBody):
    """docstring for AdmissionDoctor."""

    def __init__(self, id, name):
        super(AdmissionDoctor, self).__init__()
        MedicalBody.__init__(self, id, name)
        self.seriously_distribution = {
            'serious': 0.2,
            'less_serious': 0.7,
            'slight': 1
        }

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
