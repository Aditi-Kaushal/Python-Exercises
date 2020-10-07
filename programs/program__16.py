#choice function

n1 = int( input ("Enter the First Number:"))
n2 = int (input ("Enter the Second Number:"))

print("\n Press 1 for Addition:")
print("Press 2 for Substraction:")
print("Press 3 for Multiplication:")
print("Press 4 for Division:")

choice = int (input ("Enter Your Choice :"))

if choice == 1:
    ans = n1 + n2
    print("Sum of Given Numbers is :",ans)
elif choice == 2:
    ans = n1 - n2
    print("Difference of given Numbers is :",ans)
elif choice == 3:
    ans = n1 * n2
    print("Multiplication of give numbers is :",ans)
elif choice ==4:
    if n2 == 0:
        print("\n Division is not possible with Zero")
    else:
        ans = n1/ n2
        print("After Division of given Numbers is :",ans)
else:
    print("\n INVALID CHOICE!!")
