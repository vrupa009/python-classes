height=int(input("enter your height: "))
if height>3:
    age=int(input("enter your age: "))
    if age<12:
        bill=150
        print("bill is 150")
    elif age<=18:
        bill=200
        print("total bill is 200")
    elif age>18:
        bill=250
        print("total bill is 250")
    want_photo=input("do you to take photo(Y/N)?")
    if want_photo=='Y':
        bill=bill+50
        print(f"the total order is {bill}")
else:
    print("cant ride")