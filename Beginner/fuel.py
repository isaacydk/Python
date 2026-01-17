while True:
    fraction = input("Fraction: ")
    while True:
        try:
            n , d = fraction.split("/")
        except ValueError:
            fraction = input("Fraction: ")
        else:
            break


    try:
        n = int(n)
        d = int(d)
        try:
            p = n / d
        except ZeroDivisionError:
            pass
        if n < 0 or d < 0:
            raise ValueError()
        if n > d:
            raise ValueError()
    except ValueError:
        pass
    else:
        p = int(p * 100)  
        if p == 100 :
            print("F")
            break
        elif p == 0:
            print("E")
            break
        else:
            print(f"{p}%")
            break
    

        

