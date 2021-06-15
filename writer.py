import csv
import os

if not os.path.exists('output'):
    os.mkdir('output')

def write(item, data):
    keys = data[0].keys()
    filename = '_'.join(item.split())
    with open(f'output/{filename}.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(data)
        