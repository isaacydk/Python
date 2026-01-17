def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6: 
        return False

    for i in range(1, len(s) - 1):
        if s[i].isdigit() and s[i-1].isalpha() and s[i+1].isalpha():
           return False
        elif s[i].isdigit() and s[i-1].isalpha():
            if s[i] == 0 : return False
        elif s[i].isalpha() and s[i-1].isdigit():
            return False 
    return True
        

main()