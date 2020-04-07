from array_api import Array
import csv

arr = []
with open('data_csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        try:
            # if(row[0] == 'CREATE'): arr = Array(); continue
            # args = [x for x in [row[1], row[2]] if x != '']
            # getattr(arr, row[0].lower())(*args)
            if(row[0] == 'CREATE'):
                arr = Array()
                continue
            elif(row[0] == 'DEBUG'):
                arr.debug_print()
                continue
            elif(row[0] == 'ADD'):
                arr.add(row[1])
                continue
            elif(row[0] == 'SET'):
                arr.set(row[1], row[2])
                continue
            elif(row[0] == 'GET'):
                print(arr.get(row[1]))
                continue
            elif(row[0] == 'DELETE'):
                arr.delete(row[1])
                continue
            elif(row[0] == 'INSERT'):
                arr.insert(row[1], row[2])
                continue
            elif(row[0] == 'SWAP'):
                arr.swap(row[1], row[2])
                continue
        except Exception as e:
            print(e)


