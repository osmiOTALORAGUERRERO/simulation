import time

c = 6
m = 12

a = int(input('Your seed: '))

def mcl(seed):
    print(seed)
    newSeed = 0
    if newSeed == data:
        newSeed = (a*seed + c) % m
        time.sleep(1)
        mcl(newSeed)

mcl(data)
