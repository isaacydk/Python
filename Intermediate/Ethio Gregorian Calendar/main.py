import sys
import calendar
from datetime import date, timedelta, datetime
months = {
        1 : "Tahisas-Tir",
        2 : "Tir-Yekatit",
        3 : "Yekatit-Megabit",
        4 : "Megabit-Miyaziya",
        5 : "Miyaziya-Genbot",
        6 : "Genbot-Sena",
        7 : "Sena-Hamla",
        8 : "Hamla-Nehase",
        9 : "Nehase-paguma-Meskerem",
        10 : "Meskerem-Tekemt",
        11 : "Tekemt-Hedar",
        12 : "Hedar-Tahisas"

    }

def main():
    while True:
        print("---------------------------------------------------------------------------------------------------")
        try:
            year = int(input("Enter a year(Julian or Gregorian): "))

            print("Gregorian Year:", year , end = "          " )
            et_year = year - 8
            if et_year > 0:
                print("Ethiopian Years:", et_year, "-", et_year+1)
                print_calander(year)
            elif et_year ==-1  and et_year+1 == 0:
                print("Ethiopian Years:", et_year, "BC","-", et_year+1, "BC" )
                print_calander(year)
            else:
                print("There is Ethiopian Calandar")
                continue
            again = input("Do you want to continue?(y/n) ").lower()
            if again == "y":
                continue
            elif again == "n":
                break
            else:
                raise ValueError()
        except ValueError:
            print("Invalid input")
            continue
    
# def calender(year):
    

def converter(g_date):
    if g_date.month > 8 or (g_date.month == 8 and g_date.day >= 29):
        eth_year = g_date.year - 7
    else:
        eth_year = g_date.year - 8



    new_year = date(g_date.year, 9, 11)
    if g_date.year % 4 == 3:
        new_year = date(g_date.year, 9, 12)

    delta = (g_date - new_year).days

    if delta >= 0:
        eth_month = delta // 30 + 1
        eth_day = delta % 30 + 1
    else:
        last_new_year = date(g_date.year - 1, 9, 11)
        if (g_date.year - 1) % 4 == 3:
            last_new_year = date(g_date.year - 1, 9, 12)
        delta = (g_date - last_new_year).days
        eth_month = delta // 30 + 1
        eth_day = delta % 30 + 1

    return eth_day

def print_calander(year):
    cal = calendar.Calendar(calendar.SUNDAY)

    for month in range(1, 13):
        print("\n", calendar.month_name[month], months[month])

        print("|-----------------------------------------|")
        print("| Sun | Mon | Tue | Wed | Thu | Fri | Sat |")
        print("|-----------------------------------------|")

        weeks = cal.monthdayscalendar(year, month)

        # Print Gregorian days
        for week in weeks:
            for day in week:
                if day == 0:
                    print("|     ", end="")
                else:
                    print(f"|  {day:2d} ", end="")
            print("|")

            # Print Ethiopian days
            for day in week:
                if day == 0:
                    print("|     ", end="")
                else:
                    eth_day = converter(date(year, month, day))
                    print(f"|  {eth_day:2d} ", end="")
            print("|")
            print("|-----------------------------------------|")
if __name__ == "__main__":
    main()


