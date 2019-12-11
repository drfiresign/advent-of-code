'''Calculate the total required mass for Santa's sleigh modules.'''
import sys
import math
import logging

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.WARNING)

def calculate_total_mass(module):
    '''Performs the actual calculation'''

    if isinstance(module, list):
        return sum([calculate_total_mass(i) for i in module])

    def calculate_fuel_weight_for_mass(mass):
        logging.info('mass weighs: %s', mass)

        def calculate_fuel(i):
            fuel = math.floor(i / 3.0) - 2
            return max(fuel, 0)

        required = calculate_fuel(mass)
        additional = calculate_total_mass(required) if required > 0 else 0

        logging.info('required fuel for mass of size %s is %s', mass, required)

        return required + additional

    fuel_required = calculate_fuel_weight_for_mass(module)
    return fuel_required

if __name__ == '__main__':
    ARGUMENTS = [int(i) for i in sys.argv[1:]]
    print(calculate_total_mass(ARGUMENTS))
