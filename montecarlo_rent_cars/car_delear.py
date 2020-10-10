from car import Car
class CarDelear(object):
    """docstring for CarDelear."""

    def __init__(self, count_purchased_cars):
        super(CarDelear, self).__init__()
        self.buy_cars(count_purchased_cars)
        self.rent_value = 350
        self.idle_value = 50
        self.busy_value = 200

    def buy_cars(self, count_purchased_cars):
        pass

    #carros en ociosos o disponibles
    def cars_idle(self):
        pass

    #carros rentados o ocupados
    def cars_rented(self):
        pass

    #retorna costos de gannacia por los autos rentados
    def calculate_costs_rents(self):
        pass

    #retorna costos de perdidas por autos ociosos
    def calculate_costs_idle(self):
        pass

    #retorna costos de perdidas por no tener autos con se solicitaron
    def calculate_costs_no_available(self, requested_cars):
        pass

    #renta carros si esta disponible, retorna carros rentados y no rentados
    def rent_cars(self, requested_cars):
        pass

    #actualiza la renta de los autos
    def update_rents(self):
        pass
