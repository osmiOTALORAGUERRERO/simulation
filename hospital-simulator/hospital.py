from connectionDB import mysql, create_entities
from waiting_room import WaitingRoom
from x_ray_room import XRayRoom
from admission_doctor import AdmissionDoctor
from emergency_doctor import EmergencyDoctor
from nurse import Nurse
from patient import Patient

class Hospital(object):
    """docstring for Hospital."""

    def __init__(self):
        super(Hospital, self).__init__()
        self.waiting_room = WaitingRoom(1)
        self.x_ray_room = XRayRoom(1)
        self.patients = []
        self.adm_doctors = []
        self.eme_doctors = []
        self.nurses = []
        self.time_elapsed = 0
        self.__init_medical_body()

    def new_patient(self, patient):
        patient.id = len(self.patients)+1
        patient.name += ' '+str(patient.id)
        self.patients.append(patient)
        self.waiting_room.assign_patient(patient)
        create_entities('pacientes', patient.id, patient.name)

    def update_state(self):
        self.time_elapsed += 1
        if len(self.waiting_room.patients) > 0:
            #asignacion de pacientes a doctores de admision
            for doc in self.adm_doctors:
                if not doc.busy:
                    patient = self.waiting_room.removePatient()
                    random_adm = [random.random(), random.random()]
                    time_simulated = doc.self_simulator(random_adm[0], random[1])
                    doc.assign_patient(patient, time_simulated, random_adm[1])

        #asignacion de pacientes despues de visita al doctor de admision
        for adoc in self.adm_doctors:
            if len(adoc.waiting_patient) > 0:
                severity = adoc.waiting_patient[0]['diagnosis']
                if severity == 'serious':
                    for edoc in self.eme_doctors:
                        if not edoc.busy:
                            patient = adoc.next_waiting_patient()['patient']
                            time_simulated, random_eme = edoc.self_simulator()
                            edoc.assign_patient(patient, time_simulated, random_eme)
                elif severity == 'less_serious':
                    for nurse in self.nurses:
                        if not nurse.busy:
                            patient = adoc.next_waiting_patient()['patient']
                            time_simulated, random_eme = nurse.self_simulator()
                            nurse.assign_patient(patient, time_simulated, random_eme)
                elif severity == 'slight':
                    adoc.next_waiting_patient()

        #asignacion de pacientes deespues del doctor de urgencias
        for edoc in self.eme_doctors:
            if len(edoc.waiting_patient) > 0:
                for patient in edoc.waiting_patient:
                    if patient['process'] == 1:
                        if patient['diagnosis'] == 'x-ray':
                            next_patient = edoc.next_waiting_patient()['patient']
                            self.x_ray_room.assign_patient(next_patient)
                        elif patient['diagnosis'] == 'nurse':
                            for nurse in self.nurses:
                                if not nurse.busy:
                                    next_patient = edoc.next_waiting_patient()['patient']
                                    time_simulated, random_eme = nurse.self_simulator()
                                    nurse.assign_patient(next_patient, time_simulated, random_eme)
                for nurse in self.nurses:
                    if not nurse.busy:
                        patient = edoc.waiting_patient[0]
                        if patient['process'] == 2:#segunda vez con el doctor
                            next_patient = edoc.next_waiting_patient()['patient']
                            time_simulated, random_eme = nurse.self_simulator()
                            nurse.assign_patient(next_patient, time_simulated, random_eme)

        # asignacion a radiografia
        if len(self.x_ray_room.patients) > 0:
            if not self.x_ray_room.xray.busy:
                patient = self.x_ray_room.removePatient()
                random_adm = random.random()
                time_simulated = self.x_ray_room.xray.self_simulator(random_adm)
                self.x_ray_room.xray.assign_patient(patient, time_simulated, random_adm)

        #asignacion de paciente despues de la radiografia
        if len(self.x_ray_room.xray.waiting_patient) > 0:
            for edoc in self.eme_doctors:
                if not edoc.busy:
                    patient = self.x_ray_room.xray.next_waiting_patient()
                    time_simulated, random_eme = edoc.self_simulator()
                    edoc.assign_patient(patient, time_simulated, random_eme)

        #asignacion de paciente despues de la enfermera
        for nurse in self.nurses:
            if len(nurse.waiting_patient)>0:
                for patient in nurse.waiting_patient:
                    nurse.next_waiting_patient()


        #updateds
        self.waiting_room.update_state()
        self.x_ray_room.update_state()
        for adoc in self.adm_doctors:
            adoc.update_state()

        for edoc in self.eme_doctors:
            edoc.update_state()

        for nurse in self.nurses:
            nurse.update_state()

        self.time_elapsed += 1

    def save_state(self):
        pass

    def __init_medical_body(self):
        self.adm_doctors.append(AdmissionDoctor(1, 'Dr. Jonson', 'doctores_admision'))
        self.adm_doctors.append(AdmissionDoctor(2, 'Dra. Gina', 'doctores_admision'))

        self.eme_doctors.append(EmergencyDoctor(1, 'Dr. Sebastian'))
        self.eme_doctors.append(EmergencyDoctor(2, 'Dr. Kevin'))
        self.eme_doctors.append(EmergencyDoctor(3, 'Dra. Angie'))

        self.nurses.append(Nurse(1, 'Dr. Nicolas'))
        self.nurses.append(Nurse(2, 'Dra. Nicolas'))
        self.nurses.append(Nurse(3, 'Dra. Nicolas'))
        self.nurses.append(Nurse(4, 'Dra. Nicolas'))
        self.nurses.append(Nurse(5, 'Dra. Nicolas'))
