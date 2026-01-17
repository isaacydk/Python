def main():
    str = input()
    convert(str)
    

def convert(str):
    str = str.replace(":)", "😊")
    str = str.replace(":(", "🙁")
    print(str)

main()
