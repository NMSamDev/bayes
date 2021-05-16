import csv
# Lectura de los datos
with open('./test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    