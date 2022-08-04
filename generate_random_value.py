with open('values.txt', 'r') as input_data:
    values = [v for v in input_data.read().split(' ') if v]

from random import randint
from datetime import datetime

def generate_random_value():
    index = randint(0, len(values)-1)

    print(values[index])

    log_value(values[index])

    remove_value(index)


def log_value(value):
    log = open('_logs.txt', 'a')
    log.write(f'{datetime.now()} -> {value}\n')
    log.close()
    
    
def remove_value(i):
    values_file = open('values.txt', 'w')
    values_file.write(''.join([x+' ' for x in values[:i]+values[i+1:]]))
    values_file.close()


if __name__ == '__main__':
    if len(values) == 0:
        print('No values found!\nRun reset_values file.')
    else:
        generate_random_value()
