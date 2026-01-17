#home work

import inflect
p = inflect.engine()

names = []
while True:
    try:
        n = input("Name: ")
        names.append(n)
    except KeyboardInterrupt:
        print("Adieu, adieu, to", p.join(names))
        break
        



#  p.join(("apple", "banana", "carrot"), final_sep="")
# 'apple, banana and carrot'



# names = []
# while True:
#     try:
#         n = input("Name: ")
#         names.append(n)
#     except KeyboardInterrupt:
#         print()
#         if len(names) > 2:
#             print("Adieu, adieu, to", end = " ")
#             for name in names[0:-1]:
#                 print(f"{name}", end=", ")
#             print(f"and {names[-1]}")
#         elif len(names) == 2:
#             print(f"Adieu, adieu to {names[0]} and {names[1]}")
#         elif len(names) == 1:
#             print(f"Adieu, adieu to {names[0]}")
#         break

