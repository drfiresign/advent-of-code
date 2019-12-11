'''Calculate the total required mass for Santa's sleigh modules.'''
import sys
import math
import logging

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.WARNING)

def calculate_total_mass(module):
    '''Performs the actual calculation'''

    logging.info('module weighs: %s', module)
    if isinstance(module, list):
        return sum([calculate_total_mass(i) for i in module])

    def calculate_fuel_weight_for_mass(mass):
        def calculate_fuel(i):
            return math.floor(i / 3.0) - 2

        required_weight = calculate_fuel(mass)
        logging.info('required fuel for mass of size %s is %s', mass, required_weight)
        if required_weight > 0:
            additional_fuel_weight = calculate_total_mass(required_weight)
        else:
            return 0
        return required_weight + additional_fuel_weight

    fuel_required = calculate_fuel_weight_for_mass(module)
    # print('for a module weight of', str(module) + ',', str(fuel_required), 'fuel', 'is required')
    return fuel_required

if __name__ == '__main__':
    ARGUMENTS = [int(i) for i in sys.argv[1:]]
    print(calculate_total_mass(ARGUMENTS))
