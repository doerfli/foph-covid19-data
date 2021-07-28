import csv

lastline = []

with open('vacc_data.csv', 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        lastline = row

print(lastline)

for f in lastline[4:-2]:  # ignore received columns (might be 0)
    if f == '':
        raise BaseException('empty field in last line')
    if f == '0':
        raise BaseException('field with value 0 in last line')
    