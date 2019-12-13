'''--- Day 2: 1202 Program Alarm ---'''

data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,10,19,23,2,9,23,27,1,6,27,31,2,31,9,35,1,5,35,39,1,10,39,43,1,10,43,47,2,13,47,51,1,10,51,55,2,55,10,59,1,9,59,63,2,6,63,67,1,5,67,71,1,71,5,75,1,5,75,79,2,79,13,83,1,83,5,87,2,6,87,91,1,5,91,95,1,95,9,99,1,99,6,103,1,103,13,107,1,107,5,111,2,111,13,115,1,115,6,119,1,6,119,123,2,123,13,127,1,10,127,131,1,131,2,135,1,135,5,0,99,2,14,0,0]

def intcode(instructions):
    '''Do the work'''

    memory = instructions[:]

    address = [0, 1, 2, 3]

    def next_set():
        '''Updates each current address index by 4'''
#        print('advancing to next set of instructions')
        for i in range(0, 4):
            address[i] += 4


    def address_at(address):
        '''Returns the value from index at `address`'''
#        print('data at address', memory[address], 'is', memory[memory[address]])
        return memory[memory[address]]


    def update_memory(address, new_value):
        '''Updated the value of index at `address`'''
#        print('updating data at address', memory[address], 'to new value', new_value)
        memory[memory[address]] = new_value


    def instruction_at(opcode):
        '''Returns the operation demanded by `opcode`'''
        ops = {
            1: 'add',
            2: 'multiply',
            99: 'halt'
        }
#        print('operation at address', opcode, 'is', ops[memory[opcode]])
        return ops[memory[opcode]]


    while True:
        operation = instruction_at(address[0])
        if operation == 'add':
            new_value = address_at(address[1]) + address_at(address[2])
        elif operation == 'multiply':
            new_value = address_at(address[1]) * address_at(address[2])
        elif operation == 'halt':
            return memory
        update_memory(address[3], new_value)
        next_set()


def fix_computer(instructions, noun, verb):
    '''Halt the 1202 program alarm'''
    instructions[1] = noun
    instructions[2] = verb
    return intcode(instructions)[0]

# part 2
def attempt_to_fix_computer(d):
    for i in range(0,100):
        for j in range(0,100):
                if fix_computer(d, i, j) == 19690720:
                    return 100 * i + j, i, j


if __name__ == '__main__':
    attempt_to_fix_computer(data)
