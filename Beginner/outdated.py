month = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

while True:
    date = input("Date: ")
    try:
        mm , dd, yy = date.split("/")
        yy , mm, dd = int(yy), int(mm), int(dd)
        if mm > 12:
            raise ValueError
        print(f"{yy:02d}-{mm:02d}-{dd:02d}")
        break
    except ValueError:
        try:
            mm_dd, yy = date.split(",")
            yy = yy.strip()
            mm, dd = mm_dd.split(" ")
            mm = mm.title()
            yy , dd = int(yy), int(dd)
            if dd > 31:
                raise ValueError
            print(f"{yy:02d}-{month[mm]:02d}-{dd:02d}")
            break
        except ValueError:
            pass
