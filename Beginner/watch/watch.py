#home work
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"(http(?:s)?://)www\.youtube\.com/embed/(\w+)", s):
        return match.group(1) + "youtu.be/" + match.group(2)


...


if __name__ == "__main__":
    main()
