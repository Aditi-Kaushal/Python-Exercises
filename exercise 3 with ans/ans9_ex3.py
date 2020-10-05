##Question 9: - The policy followed by a company to process customer orders is given by the following
##rules:
##    (a) If a customer order is less than or equal to that in stock and has credit is OK, supply has
##requirement.
##(b) If has credit is not OK do not supply. Send him intimation.
##(c) If has credit is Ok but
##the item in stock is less than has order, supply what is in stock. Intimate to him data the balance will
##be shipped. Write a C program to implement the company policy.

order= int (input ("Enter your order:"))
credit = str(input ("Enter the CREDIT :ok or not ok:"))
stock = 500
if order <= stock:
    if credit == "ok":
        print("Supply has Requirement")
    else:
        print("NO SUPPLY!,Intimation")
else:
    if credit =="ok":
        supply = order-stock
        print("ITEM in the STOCK is lesser than the ORDER soo,THE Available Items are :",order-supply,"||","items left:",supply)
    else:
        print("NO SUPPLY!!")
    
