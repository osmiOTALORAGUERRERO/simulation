from randomic import Random
from testing import Testing

random_set = Random()
test_driver = Testing()

def options_random(entry):
    if entry == 1:
        while True:
            try:
                path = input("Enter the file path: \n")
                random_set.load_file(path)
                break
            except Exception as e:
                print(e)
    elif entry == 2:
        while True:
            try:
                max = input("Enter the max of numbers to generate: \n")
                random_set.load(int(max))
                break
            except Exception as e:
                print(e)


def options_test():
    test = int(input("1. distance \nx. :) \n"))
    return test

entry_random = 0

while True:
    entry_random = int(input("1. file \n2. default \n"))
    if entry_random == 1 or entry_random == 2:
        break
options_random(entry_random)
opt_test = options_test()
test_case = test_driver.target(opt_test, random_set.set)
X2, OF, EF = test_case.outcome()
print('numbers set:', random_set.set)
print('')
print('FO:',OF)
print('')
print('FE:',EF)
print('')
print('n:', len(OF)-1)
print('X2:',X2)
