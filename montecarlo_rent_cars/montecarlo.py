import random
from car import Car
from car_delear import CarDelear

class Montecarlo(object):
    """docstring for Montecarlo."""

    def __init__(self):
        super(Montecarlo, self).__init__()
        self.max_cars = 4
        #tabla anual
        self.table_by_purchased_cars = {
            'days' : [],
            'cars_request': [],
            'days_cars_rented': {},
            'cars_rented':[],
            'cars_idle':[],
            'cars_no_rent':[],
            'costs_rents':[],
            'costs_idle':[],
            'costs_no_rent':[]
        }
        #tabla que almacena el resultado de las tablas anuales
        self.table_result_final = {}
        self.annual_auto_cost = 75000
        self.days = 365
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
        self.automatic = False

    def run(self, purchased_cars=None):
        if purchased_cars == None:
            for i in range(self.max_cars+1):
                self.annual_simulation(i)
            self.print_table_final()
        else:
            self.annual_simulation(purchased_cars)

    def annual_simulation(self, purchased_cars):
        self.car_delear = CarDelear(purchased_cars)
        for i in range(1, purchased_cars+1):
            self.table_by_purchased_cars['days_cars_rented']['car'+str(i)]=[]

        for day in range(1, self.days+1):
            self.car_delear.update_rents()
            self.day_simulation(self.cars_rented_day(random.random()))
            self.table_by_purchased_cars['days'].append(day)

        self.print_table_annual(purchased_cars)
        self.update_table_final(purchased_cars)
        self.restart_table_annual()

    def day_simulation(self, rented_cars):
        self.table_by_purchased_cars['cars_request'].append(rented_cars)
        self.table_by_purchased_cars['cars_no_rent'].append(self.car_delear.cars_no_rented(rented_cars))
        self.table_by_purchased_cars['costs_no_rent'].append(self.car_delear.calculate_costs_no_available(rented_cars))

        for i in range(rented_cars):
            rent_days = self.days_of_car_rent(random.random())
            rented = self.car_delear.rent_car(rent_days)
        for car_i in range(len(self.car_delear.purchased_cars)):
            car_days = self.car_delear.purchased_cars[car_i].rent_days
            self.table_by_purchased_cars['days_cars_rented']['car'+str(car_i+1)].append(car_days)


        self.table_by_purchased_cars['cars_rented'].append(self.car_delear.cars_rented)
        self.table_by_purchased_cars['cars_idle'].append(self.car_delear.cars_idle)
        self.table_by_purchased_cars['costs_rents'].append(self.car_delear.calculate_costs_rents())
        self.table_by_purchased_cars['costs_idle'].append(self.car_delear.calculate_costs_idle())


    def cars_rented_day(self, p_of_rented_cars):
        if p_of_rented_cars<self.historical_rented_cars['0']:
            return 0
        if p_of_rented_cars<self.historical_rented_cars['1']:
            return 1
        if p_of_rented_cars<self.historical_rented_cars['2']:
            return 2
        if p_of_rented_cars<self.historical_rented_cars['3']:
            return 3
        if p_of_rented_cars<self.historical_rented_cars['4']:
            return 4

    def days_of_car_rent(self, p_of_days_rented):
        if p_of_days_rented<self.historical_rented_days['1']:
            return 1
        if p_of_days_rented<self.historical_rented_days['2']:
            return 2
        if p_of_days_rented<self.historical_rented_days['3']:
            return 3
        if p_of_days_rented<self.historical_rented_days['4']:
            return 4

    def update_table_final(self, purchased_cars):
        self.table_result_final['purchased_cars'+str(purchased_cars)] = {}
        gross_profit = 0
        neto_profit = 0
        loss_idle = 0
        loss_no_rent = 0
        loss_total = 0
        goal = self.annual_auto_cost * purchased_cars
        for i in range(self.days):
            gross_profit += self.table_by_purchased_cars['costs_rents'][i]
            loss_idle += self.table_by_purchased_cars['costs_idle'][i]
            loss_no_rent += self.table_by_purchased_cars['costs_no_rent'][i]

        loss_total = loss_idle + loss_no_rent
        neto_profit = gross_profit - loss_total
        reached = neto_profit >= goal

        self.table_result_final['purchased_cars'+str(purchased_cars)]['purchased_cars'] = purchased_cars
        self.table_result_final['purchased_cars'+str(purchased_cars)]['gross_profit'] = gross_profit
        self.table_result_final['purchased_cars'+str(purchased_cars)]['loss_idle'] = loss_idle
        self.table_result_final['purchased_cars'+str(purchased_cars)]['loss_no_rent'] = loss_no_rent
        self.table_result_final['purchased_cars'+str(purchased_cars)]['loss_total'] = loss_total
        self.table_result_final['purchased_cars'+str(purchased_cars)]['neto_profit'] = neto_profit
        self.table_result_final['purchased_cars'+str(purchased_cars)]['goal'] = goal
        self.table_result_final['purchased_cars'+str(purchased_cars)]['reached'] = reached

    def restart_table_annual(self):
        self.table_by_purchased_cars = {
            'days' : [],
            'cars_request': [],
            'days_cars_rented': {},
            'cars_rented':[],
            'cars_idle':[],
            'cars_no_rent':[],
            'costs_rents':[],
            'costs_idle':[],
            'costs_no_rent':[]
        }

    def print_table_annual(self, purchased_cars):
        import os
        import time
        tbpc = self.table_by_purchased_cars
        path = os.getcwd()+'\\reports\\'+'table-annual'+str(time.time())+'pc'+str(purchased_cars)+'.csv'
        fw = open(path,'w')
        header = 'days, cars_request, '
        for car in tbpc['days_cars_rented']:
            header += car+', '
        header += 'cars_rented, cars_idle, cars_no_rent, costs_rents, costs_idle, costs_no_rent\n'
        fw.write(header)
        body = ''
        for day in range(self.days):
            for row in tbpc:
                if row == 'days_cars_rented':
                    for dcr in tbpc[row]:
                        body += str(tbpc[row][dcr][day])+', '
                    continue
                if row == 'costs_no_rent':
                    body += str(tbpc[row][day])+'\n'
                    continue
                body += str(tbpc[row][day])+', '
        fw.write(body)
        fw.close()
        tbpc = None
        # print(self.table_by_purchased_cars)

    def print_table_final(self):
        import os
        import time
        trf = self.table_result_final
        path = os.getcwd()+'\\reports\\'+'table-final'+str(time.time())+'.csv'
        fw = open(path,'w')
        header = 'purchased_cars, gross_profit, loss_idle, loss_no_rent, loss_total, neto_profit, goal, reached\n'
        body = ''
        for result in trf:
            for row in trf[result]:
                if row == 'reached':
                    body += str(trf[result][row])+'\n'
                    continue
                body += str(trf[result][row])+', '
        fw.write(header)
        fw.write(body)
        fw.close()
        trf = None
        # print(self.table_result_final)
