from montecarlo import Montecarlo

while True:
    simulator = Montecarlo()
    mode = int(input('Modo de ejecucion: \n1. Automatico(0-4) \n2. Manual\n'))
    if mode != 1 and mode != 2:
        print('No selecciono ningun modo')
        break
    if mode==1:
        simulator.run()
        continue
    if mode==2:
        while True:
            purchased_cars = input('Indique los autos adquiridos: | n: terminar\n')
            if purchased_cars == 'n':
                simulator.print_table_final()
                break
            if int(purchased_cars) >= 0:
                simulator.run(int(purchased_cars))
        continue

print('Simulador terminado')
