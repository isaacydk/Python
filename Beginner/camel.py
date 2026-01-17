camelCase = input("camelCase: ")
snake_case = ""
for ch in camelCase :
    if ch.islower():
        snake_case += ch
    else:
        snake_case += "_" + ch.lower()
print("snake_case:", snake_case)