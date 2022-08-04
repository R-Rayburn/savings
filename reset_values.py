from datetime import datetime


def reset_values():
    values = open('values.txt', 'w')
    values.write(''.join([str(x)+' ' for x in range(1, 101)]))
    values.close()
    

def log_reset():
    log = open('_logs.txt', 'a')
    log.write(f'\nReset on {datetime.now()}')
    log.close()


if __name__ == "__main__":
    reset_values()
    log_reset()
