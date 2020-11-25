from connectionDB import mysql
from waiting_room import WaitingRoom
from x_ray_room import XRayRoom
from admission_doctor import AdmissionDoctor
from emergency_doctor import EmergencyDoctor
from nurse import nurse
from patient import Patient

class Hospital(object):
    """docstring for Hospital."""

    def __init__(self):
        super(Hospital, self).__init__()
        self.waiting_room = WaitingRoom(1)
        self.x_ray_room = XRayRoom(1)
        self.patients = []
        self.adm_doctor = []
        self.eme_doctor = []
        self.nurse = []
        self.time_elapsed = 0

    def newPatient(self, patient):
        pass

    def update_state(self, arg):
        pass

    def save_state(self, arg):
        pass

    def __init_medical_body():
        self.adm_doctor.append()
