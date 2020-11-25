from connectionDB import mysql

class Patient(object):
    """docstring for Patient."""

    def __init__(self, id):
        super(Patient, self).__init__()
        self.id = id
        self.name = name
        self.final_time = 0

    def update_state(self, arg):
        self.final_time += 1

    def state_capture(self, arg):
        pass
