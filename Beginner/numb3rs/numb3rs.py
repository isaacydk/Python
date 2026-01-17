#home work
import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^(?:[1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(?:\.(?:[1-9]?\d|1\d\d|2[0-4]\d|25[0-5])){3}$"
    return bool(match := re.search(pattern, ip))
      


if __name__ == "__main__":
    main()