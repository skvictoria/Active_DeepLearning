import csv

with open('val_labels.csv', 'r') as inp, open('val_lower.csv', 'w') as outjpg, open('val_bigger.csv', 'w') as outJPG:
    csv_f = csv.reader(inp)
    csv_jpg = csv.writer(outjpg)
    csv_JPG = csv.writer(outJPG)
    for line in csv_f:
        if line[3]!="normal" and line[3]!="dry" and line[0].endswith('jpg'):
            csv_jpg.writerow(line)
        elif line[3]!="normal" and line[3]!="dry" and line[0].endswith('JPG'):
            csv_JPG.writerow(line)
            
with open('train_labels.csv', 'r') as inp, open('train_lower.csv', 'w') as outjpg, open('train_bigger.csv', 'w') as outJPG:
    csv_f = csv.reader(inp)
    csv_jpg = csv.writer(outjpg)
    csv_JPG = csv.writer(outJPG)
    for line in csv_f:
        if line[3]!="normal" and line[3]!="dry" and line[0].endswith('jpg'):
            csv_jpg.writerow(line)
        elif line[3]!="normal" and line[3]!="dry" and line[0].endswith('JPG'):
            csv_JPG.writerow(line)
