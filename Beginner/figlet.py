#home work
import sys
import pyfiglet
from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv) == 1:
    ordinary = input("Input: ")
    print(figlet.renderText(ordinary))
    sys.exit()
elif len(sys.argv) == 3: 
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
     
        try:
            figlet.setFont(font = sys.argv[2])
        except pyfiglet.FontNotFound:
            sys.exit("Invalid usage")
            
        ordinary = input("Input: ") 
        print(figlet.renderText(ordinary))
        sys.exit()
    else:
        sys.exit("Invalid usage")
    # 
elif len(sys.argv) == 2:
    sys.exit("Invalid usage")




