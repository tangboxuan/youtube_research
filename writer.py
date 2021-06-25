import csv
import os

if not os.path.exists('output'):
    os.mkdir('output')

def write(time, item, data):
    if not os.path.exists(f'output/{time}'):
        os.mkdir(f'output/{time}')
    keys = data[0].keys()
    filename = '_'.join(item.split())
    with open(f'output/{time}/{filename}.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(data)
        