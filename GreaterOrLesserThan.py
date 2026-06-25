num = int(input("Enter Number to Check :"))

if num>50:
    print("Number is greater than 50")
    if num%2==0:
        print("And it is Even too")
    else:
        print("And it is odd")

else:
    print("Number is less than 50")