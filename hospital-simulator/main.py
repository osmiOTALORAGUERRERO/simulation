from simulator import Simulator

min = int(input('Tiempo de simulacion en min'))
print(min)
h_simulator = Simulator(min)
h_simulator.run()
