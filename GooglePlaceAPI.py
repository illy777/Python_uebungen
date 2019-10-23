import os
import csv

table = ["1","2","3"]
file_name = "Test1.csv"

n = os.path.exists(file_name)

print(n)

if os.path.exists(file_name) is True:
    with open(file_name, 'a') as file:
        csv_writer = csv.writer(file, delimiter=',', quoting= csv.QUOTE_ALL)
        csv_writer.writerows(table)
else:
    with open(file_name, 'w') as file:
        csv_writer = csv.writer(file, delimiter=',', quoting= csv.QUOTE_ALL)
        csv_writer.writerows(table)

