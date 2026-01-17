#home work
import re

def main():
    print(convert(input("Hours: ")))

def convert(hrs):
    pattern = r"^(?P<starthrs>(1[0-2])|[1-9])(?P<startmin>\:[0-5]\d)? (?P<sm>AM|PM) to (?P<endhrs>(1[0-2])|[1-9])(?P<endmin>\:[0-5]\d)? (?P<em>AM|PM)$"
    match = re.search(pattern, hrs)

    if not match:
        raise ValueError("Invalid time format")
    
    match = re.search(pattern, hrs)
    if not match:
        raise ValueError("Invalid time format")

    start_time = to_24h(
        match.group("starthrs"),
        match.group("startmin"),
        match.group("sm"),
    )

    end_time = to_24h(
        match.group("endhrs"),
        match.group("endmin"),
        match.group("em"),
    )

    return f"{start_time} to {end_time}"
    
         
def to_24h(hr, min, m):
    hr = int(hr)
    min = min[1:] if min else "0"
    min = int(min)

    if m == "AM":
        if hr == 12:
            hr = 0
    else:
        if hr != 12:
            hr += 12
    return f"{hr:02}:{min:02}"


if __name__ == "__main__":
    main()