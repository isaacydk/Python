#home work

import sys

if len(sys.argv) == 2:
    try:
        name, type = sys.argv[1].split(".") 
        if type != "py":
            raise ValueError()
    except ValueError:
        sys.exit("Not a Python file")
    except TypeError:
        sys.exit("Not a Python file")
           
    try:   
        with open(sys.argv[1]) as f:
            lines = f.readlines()
            total = len(lines)
            for line in lines:
                if line[0] == "#":
                    total -= 1
                elif line == "\n":
                    total -= 1
        
        print(total)
    except FileNotFoundError:
        sys.exit("File does not exist")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")
else:
    sys.exit("Too few command-line argument")