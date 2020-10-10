class Car(object):
    """docstring for Car."""

    def __init__(self):
        super(Car, self).__init__()
        self.rent = false
        self.rent_days = 0

    def rent_car(self, rent_days):
        if !self.rent:
            self.rent_days = rent_days
            self.rent = true
            return True
        return False

    def update_rent_days(self):
        if self.rent:
            self.rent_days -= 1
            if self.rent_days == 0:
                self.rent = False
            return True
        return False
