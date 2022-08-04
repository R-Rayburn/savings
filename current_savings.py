with open('_logs.txt', 'r') as input_data:
    values = [v for v in input_data.read().split('\n') if v]

def print_total_savings():
    totals = 0
    for v in values:
        
        totals += int(v.split(' -> ')[1])

    print(f"Number of days: {len(values)}")
    print(f"Total Savings: {totals}")


if __name__ == '__main__':
    print_total_savings()
