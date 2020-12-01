from medical_body import MedicalBody
from connectionDB import mysql

class Nurse(MedicalBody):
    """docstring for AdmissionDoctor."""

    def __init__(self, id, name, table=''):
        super(Nurse, self).__init__()
        MedicalBody.__init__(self, id, name, 'enfermeras')

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
                minutes = 7.5+2.92*(random_sum-6)
            if minutes > 0:
                break
        return int(minutes), random_sum
