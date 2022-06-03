m=float(input('What is your maximum to spend? '))
g=0
t=0
c=0
av=m
a=0
while g<=m:
    print("You have $",av," dollars to spend.\nSelect the items by choosing the number of the item from the list below or 0 to check out.")
    print("1) Roses = $75 per 1/2 dozen (25% discount)\n2) Hair extensions = $100 per pack (10% discount)\n3) Male Jeans = $150\n4) Female jeans = $175 (5% discount)\n5) Jordans = $200")
    i=int(input("Enter the number corresponding to the number you desire: "))
    if i==0:
        print("You have decided to stop shopping!")
        print("You have spent ",g," dollars!")
        g=m*2
    elif i==1:
        a=int(input("Select the amount: "))
        t=((a*75)*0.75)
    elif i==2:
        a=int(input("Select the amount: "))
        t=((a*100)*0.9)
    elif i==3:
        a=int(input("Select the amount: "))
        t=(a*150)
    elif i==4:
        a=int(input("Select the amount: "))
        t=((a*175)*0.95)
    elif i==5:
        a=int(input("Select the amount: "))
        t=(a*200)
    t=t-(t*0.07)
    c=c+a
    if t>av:
        print("You do not have enough money for that purchase!")
        c=c-a
        print("You have ",c," items in your cart!")
        t=0
    elif t<=av:
        print("You have ",c," items in your cart!")
    g=g+t
    av=m-g
    a=0
