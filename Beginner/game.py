import random

while True:
    try:
        n = int(input("Level: "))
        if n <= 0:
            raise ValueError()
        r = random.randint(1, n)
        guess = 0
        while True:
            try:
                guess = int(input("Guess: "))
                if guess <= 0:
                    raise ValueError()
                
                if guess > r:
                    print("Too large!")
                elif guess < r:
                    print("Too small!")
                else:
                    print("Just right!")
                    break
            except ValueError:
                    pass
        
        break
        
    except ValueError:
        pass