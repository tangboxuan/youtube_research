import csv
import os

if not os.path.exists('output'):
    os.mkdir('output')

def write(time, item, data, page, english):
    filename = item + ('-EN' if english else '')
    if not os.path.exists(f'output/{time}'):
        os.mkdir(f'output/{time}')
    if not os.path.exists(f'output/{time}/{item}'):
        os.mkdir(f'output/{time}/{item}')
    keys = (data[0].keys())
    with open(f'output/{time}/{item}/{filename}.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, keys)
        if not page:
            writer.writeheader()
        writer.writerows(data)
        