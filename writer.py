import csv
import os

if not os.path.exists('output'):
    os.mkdir('output')

def write(time, item, data, page):
    if not os.path.exists(f'output/{time}'):
        os.mkdir(f'output/{time}')
    keys = data[0].keys()
    filename = '_'.join(item.split())
    with open(f'output/{time}/{filename}.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, keys)
        if not page:
            writer.writeheader()
        writer.writerows(data)
        