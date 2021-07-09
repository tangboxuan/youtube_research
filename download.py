import youtube_dl
import os
import inquirer
import csv

ydl_opts = {
    "writesubtitles": True,
    "writeautomaticsub": True
}


def download():
    folderQ = [inquirer.List(
        'folder', 
        message="Choose download folder", 
        choices=[f for f in os.listdir(os.getcwd()+'/output') if not f.startswith('.')]
    )]
    folderA = inquirer.prompt(folderQ)['folder']
    productQ = [inquirer.List(
        'product', 
        message="Choose product", 
        choices=[f for f in os.listdir(os.getcwd()+'/output/'+folderA) if not f.startswith('.')]
    )]
    productA = inquirer.prompt(productQ)['product']
    fileQ = [inquirer.List(
        'file', 
        message="Choose CSV file", 
        choices=[f for f in os.listdir(f"{os.getcwd()}/output/{folderA}/{productA}") if f.endswith('.csv') and not f.startswith('.')]
    )]
    fileA = inquirer.prompt(fileQ)['file']
    os.chdir(f'output/{folderA}/{productA}')
    links = []
    with open(fileA, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line in csv_reader:
            links.append(line['link'])
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)

if __name__ == "__main__":
    download()