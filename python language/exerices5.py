#piza order program
size=(input("enter the size of the piza(s/m/l)? "))
bill=0
if size=='s':
    bill=100
    print('bill is 100')
elif size=='m':
    bill=200
    print("bill is 200")
elif size=='l':
    bill=300
    print("bill is 300")
want=input("do you want peper(Y/N)?")
if want=='y':
    if size=='s':
        bill=bill+50
        print(f"the total bill is{bill}")
    elif size=='m':
        bill=bill+100
        print(f"the total bill is{bill}")
    else:
        bill=bill+150
        print(f"the total bill is{bill}")
    want_1=input("do you want extra chees(Y/N)?")
    if want_1=='y':
        bill=bill+50
        print(f"total is {bill}")
else:
    print("thanku for ordering")
print("bye")
        