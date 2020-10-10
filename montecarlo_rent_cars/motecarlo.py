import random
from car_delear import CarDelear

class Montecarlo(object):
    """docstring for Montecarlo."""

    def __init__(self):
        super(Montecarlo, self).__init__()
        self.car_delear
        self.table_by_purchased_cars = {
            'days' : [],
            'cars_request': [],
            'days_cars_rented': {},
            'cars_rented':[],
            'cars_idle':[],
            'cars_no_available':[],
            'costs_rents':[],
            'costs_costs_idle':[],
            'costs_no_available':[]
        }
        self.table_result_final = {}
        self.annual_auto_cost = 75000
        self.historical_rented_cars = {
            '0' : 0.10,
            '1' : 0.20,
            '2' : 0.45,
            '3' : 0.75,
            '4' : 1
        }
        self.historical_rented_days = {
            '1' : 0.4,
            '2' : 0.75,
            '3' : 0.90,
            '4' : 1
        }

        def run(self, arg):
            
            pass

        def annual_simulation(self, arg):
            pass

        def day_simulation(self, arg):
            pass

        def print_tables(self, arg):
            pass
