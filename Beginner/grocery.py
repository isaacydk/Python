grocery_list = []
while True:
    try:
        groceres = input()
        grocery_list.append(groceres)
    except KeyboardInterrupt:
        print()
        grocery_list.sort()
        for grocery in grocery_list:
            try:
                if grocery_list.count(grocery) > 1:
                    print(grocery_list.count(grocery), grocery.upper())
                    grocery_list = grocery_list.remove(grocery)
                else:
                    print(grocery_list.count(grocery), grocery.upper())
            except AttributeError:
                pass
            except KeyboardInterrupt:
                pass
        break
