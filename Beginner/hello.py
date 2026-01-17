while True:
    try:
        x = int(input("x: "))
    except ValueError:
        print("x is not an integer")
    else:
        print(f"x is {x}")
        break
