max=float(input("What is your maximum to spend? "))
c=0
g=0
av=max
total=0
while g<=max:
    print("You have $",av," dollars to spend. Select the items by choosing the number of the item from the list below or 0 to check out.")
    print("1) Roses = $75 per 1/2 dozen (25% discount)  \n2) Hair extensions = $100 per pack (10% discount)  \n3) Male Jeans = $150  \n4) Female jeans = $175 (5% discount)  \n5) Jordans = $200")
    i=int(input("Enter the number corresponding to the number you desire: "))
    if i==0:
        print("You have decided to stop shopping!")
        print("You have ",c," items in your cart and spent ",g," dollars!")
        g=max*2
    else:
        if i==1:
            a=int(input("Select the amount: "))
            total= a * 75 * 0.75
        if i==2:
            a=int(input("Select the amount: "))
            total= a * 100 * 0.9
        if i==3:
            a=int(input("Select the amount: "))
            total= a * 150
        if i==4:
            a=int(input("Select the amount: "))
            total = a * 175 * 0.95
        if i==5:
            a=int(input("Select the amount: "))
            total = a * 200
        total=total+(total*0.07)
        c=c+a
        if total>av:
            print("You do not have enough money for that purchase!")
            c=c-a
            print("You have ",c," items in your cart!")
            total=0
        else:
            print("You have ",c," items in your cart!")
        g=g+total
        av=max-g
