import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames= ["name", "home"])
    writer.writerow({"name": name, "home": home})



















# import csv

# students = []

# with open("students.csv", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({
#             "name": row["name"],
#             "home": row["home"]
#         })

# for student in sorted(students, key=lambda s: s["name"]):
#     print(f"{student['name']} is in {student['home']}")



# with open("students.csv") as file:
#     for line in sorted(file):
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

#using dictionary and list