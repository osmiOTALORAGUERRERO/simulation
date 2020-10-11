from car import Car

class CarDelear(object):
    """docstring for CarDelear."""

    def __init__(self, count_purchased_cars):
        super(CarDelear, self).__init__()
        self.purchased_cars = []
        self.rent_value = 350
        self.idle_value = 50
        self.busy_value = 200
        self.buy_cars(count_purchased_cars)

    def buy_cars(self, count_purchased_cars):
        for i in range(int(count_purchased_cars)):
            self.purchased_cars.append(Car())

    #carros en ociosos o disponibles
    @property
    def cars_idle(self):
        quantity = 0
        for car in self.purchased_cars:
            if not car.rent:
                quantity += 1
        return quantity


    #carros rentados o ocupados
    @property
    def cars_rented(self):
        quantity = 0
        for car in self.purchased_cars:
            if car.rent:
                quantity += 1
        return quantity

    def cars_no_rented(self, requested_cars):
        return abs(self.cars_idle-requested_cars)

    #retorna costos de gannacia por los autos rentados
    def calculate_costs_rents(self):
        value = self.cars_rented*self.rent_value
        return value

    #retorna costos de perdidas por autos ociosos
    def calculate_costs_idle(self):
        value = self.cars_idle*self.idle_value
        return value

    #retorna costos de perdidas por no tener autos con se solicitaron
    def calculate_costs_no_available(self, requested_cars=None, no_rented=None):
        if requested_cars != None:
            availability = self.cars_idle-requested_cars
            if availability < 0:
                return abs(availability)*self.busy_value
        if no_rented != None:
            return abs(availability)*self.busy_value
        return 0

    #renta carros si esta disponible, retorna carros rentados y no rentados
    def rent_car(self, rent_days):
        rented = False
        for car in self.purchased_cars:
            if not car.rent:
                car.rent_car(rent_days)
                rented = True
                break
        return rented

    #actualiza la renta de los autos
    def update_rents(self):
        for car in self.purchased_cars:
            if car.rent:
                car.update_rent_days()
