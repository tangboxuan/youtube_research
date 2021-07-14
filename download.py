import youtube_dl
import os
import inquirer
import csv
from vtt_to_srt.vtt_to_srt import vtt_to_srt

ydl_opts = {
    "writesubtitles": True,
    "writeautomaticsub": True,
    "skip_download": True,
}

foldername = "07-14_21:58:40"
productname = "Sony_wf-1000xm4"
filename = "Sony_wf-1000xm4-EN.csv"

def download():
    links = []
    os.chdir(f'output/{foldername}/{productname}')
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line in csv_reader:
            links.append(line['link'])
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)
    for f in os.listdir():
        if f.endswith('.vtt'):
            vtt_to_srt(f)
            os.remove(f)
    for f in os.listdir():
        if f.endswith('.srt'):
            cleaned = []
            previous = ""
            with open(f, 'r') as srt_file:
                content = srt_file.readlines()
                for line in content:
                    words = line.split()
                    if len(words) > 1 and words[1] != "-->" and line != previous:
                        cleaned.append(line)
                        previous = line
            with open(f[:-3]+'.txt', 'w') as txt_file:
                txt_file.write(''.join(cleaned))
            os.remove(f)

# def download():
#     folderQ = [inquirer.List(
#         'folder', 
#         message="Choose download folder", 
#         choices=[f for f in os.listdir(os.getcwd()+'/output') if not f.startswith('.')]
#     )]
#     folderA = inquirer.prompt(folderQ)['folder']
#     productQ = [inquirer.List(
#         'product', 
#         message="Choose product", 
#         choices=[f for f in os.listdir(os.getcwd()+'/output/'+folderA) if not f.startswith('.')]
#     )]
#     productA = inquirer.prompt(productQ)['product']
#     fileQ = [inquirer.List(
#         'file', 
#         message="Choose CSV file", 
#         choices=[f for f in os.listdir(f"{os.getcwd()}/output/{folderA}/{productA}") if f.endswith('.csv') and not f.startswith('.')]
#     )]
#     fileA = inquirer.prompt(fileQ)['file']
#     os.chdir(f'output/{folderA}/{productA}')
#     links = []
#     with open(fileA, 'r') as csv_file:
#         csv_reader = csv.DictReader(csv_file, delimiter=',')
#         for csv_line in csv_reader:
#             print("Downloading captions for "+csv_line['title'])
#             yt = YouTube(csv_line['link'])
#             try:
#                 ytcaption = yt.captions['en-US']
#                 caption = ytcaption.generate_srt_captions().split('\n')
#                 cleaned = []
#                 for i in range(len(caption)):
#                     if i % 4 == 2:
#                         cleaned.append(caption[i])
#                 with open(csv_line['title']+'.txt', 'w') as f:
#                     f.write('\n'.join(cleaned))
#             except KeyError:
#                 continue

if __name__ == "__main__":
    download()