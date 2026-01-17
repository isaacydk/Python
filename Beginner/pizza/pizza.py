#home work
import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 2:
    try:
        name, type = sys.argv[1].split(".") 
        if type != "csv":
            raise ValueError()
    except ValueError:
        sys.exit("Not a CSV file")
    except TypeError:
        sys.exit("Not a CSV file")
           
    try:   
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            table = []
            for row in reader:
                table.append(row)
            print(tabulate(table , headers="keys", tablefmt="grid" ))
    except FileNotFoundError:
        sys.exit("File does not exist")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")
else:
    sys.exit("Too few command-line argument")