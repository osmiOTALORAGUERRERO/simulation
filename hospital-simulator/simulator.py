import math
import random
from hospital import Hospital
from patient import Patient
from connectionDB import truncate_tables

names_patients = [
    'Maria Carmen',
    'Jose Antonio',
    'Ana Maria',
    'Jose Luis',
    'Maria Pilar',
    'Francisco Javier',
    'Maria Dolores',
    'Jose Manuel',
    'Maria Teresa',
    'Carlos',
    'Antonia',
    'David',
    'Dolraores',
]

class Simulator(object):
    """docstring for Simulator."""

    def __init__(self, execution_time):
        super(Simulator, self).__init__()
        truncate_tables()
        self.hospital = Hospital()
        self.execution_time = execution_time
        self.new_patient = {'patient': None, 'time_elapsed':None}
        self.distributions = self.__patient_distribution()

    def run(self):
        random_patient = random.random()
        self.new_patient['patient'] =  Patient(0 ,names_patients[random.randrange(len(names_patients))])
        self.new_patient['time_elapsed']= self.patient_simulator(random_patient)
        print(self.new_patient['patient'])
        self.new_patient['patient'].random_time = random_patient
        for min in range(self.execution_time):
            self.minute_simulation(min)

    def minute_simulation(self, min):
        if self.new_patient['time_elapsed'] <= 0:
            random_patient = random.random()
            self.hospital.new_patient(self.new_patient['patient'])
            self.new_patient['patient'] = Patient(0 ,names_patients[random.randrange(len(names_patients))])
            self.new_patient['time_elapsed'] = self.patient_simulator(random_patient)
            self.new_patient['patient'].random_time = random_patient

        self.new_patient['time_elapsed'] -= 1

        self.hospital.update_state()
        # self.hospital.save_state()

    def patient_simulator(self, R):
        i = 0
        for dist in self.distributions:
            if R < dist:
                return i
            i += 1

    def __patient_distribution(self):
        distribution = []
        sum_distribution = 0
        i = 0
        while True:
            dist = ((math.exp(-7))*(7**i))/math.factorial(i)
            sum_distribution += round(dist, 2)
            distribution.append(sum_distribution)
            i += 1
            if int(sum_distribution)>=1:
                break;

        return distribution
