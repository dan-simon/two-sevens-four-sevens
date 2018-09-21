import random

def to_percent(x):
    return float(x.replace('%', ''))

while True:
    question = input('> ')
    percent_list = [to_percent(i) for i in question.split(' ') if '%' in i]
    percent = (percent_list + [50])[0]
    print('yes' if random.random() < percent * 1e-2 else 'no')
