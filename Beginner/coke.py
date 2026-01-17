amount_due = 50
print("Amount Due:", amount_due)

while True:
    insert_coin = int(input("Insert coin: "))
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        amount_due -= insert_coin
        if amount_due == 0:
            print("Change owed:", 0)
            break
        elif amount_due < 0:
            print("Change owned: ", abs(amount_due) )
            break
        else:
            print("Amount due: ", amount_due)
    else:
        print("Amount Due:", amount_due)
        
