print ("Amount Due: 50")
amountDue = int(50)

insertCoin = int(input("Insert Coin: "))



while amountDue!=0:
    amountDue = amountDue - insertCoin
    if amountDue != 0: 
        print("Amount Due:", amountDue)
        insertCoin = int(input("Insert Coin: "))
    while amountDue == 0:
        print("change owned: 0")
        break
    
    
