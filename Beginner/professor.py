#home work
import random


def main():
    n = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        for z in range(3):
            print(x, "+", y, "= ", end = "")
            try:
                answer = int(input())
                if answer == x + y:
                    score += 1
                    break
                else:
                    raise ValueError

            except ValueError:
                print("EEE")
                pass
            if z == 2:
                    print(x, "+", y, "=", x+y)
    print("Score:", score)

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n == 1 or n == 2 or n ==3:
                return n    
            else:
                raise ValueError()
        except ValueError:
            pass



def generate_integer(level):
    if level == 1:
        return random.randint(1,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()