from connectionDB import mysql, create_entities
from x_ray import XRay

class XRayRoom(object):
    """docstring for XRayRoom."""

    def __init__(self, id):
        super(XRayRoom, self).__init__()
        self.id = id
        self.xray = XRay(1)
        self.patients = []
        create_entities('sala_radiografia', self.id )

    def assign_patient(self, patient):
        self.patients.append(patient)

    def removePatient(self):
        self.patients.pop(0)

    def update_state(self):
        for patient in self.patients:
            patient.update_state()
        self.xray.update_state()
