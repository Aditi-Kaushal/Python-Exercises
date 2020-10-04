'''Question 22: - Write a Program to calculate and print the Electricity bill of a given customer. The
Customer ID and unit consumed by the user should be taken from the keyboard and display the total
amount to pay by the customer. The charge are as follows:
      Unit                             Charge Per Unit
Upto 199                              @1.20
200 and above but less than 400       @1.50
400 and above but less than 600       @1.80
600 and above @2.00
If bill exceeds Rs. 400 then a surcharge of 15% will be charged and the minimum bill should be of Rs.
200.'''

customer_id= int (input ("Enter the Customer ID:"))
unit= int (input ("Enter the Unit Consumed by the customer:"))
if unit > 0:
    if unit < 199:
        charge = unit *1.20
        print("Amount to pay for upto 199 units is RS:",charge,"/-")
    else:
        if unit < 400 :
            charge = unit * 1.50
            print("Amount to pay for 200 to 400 units  is RS:",charge,"/-")
        else:
            if unit < 600:
                charge = unit * 1.80
                print("Amount to pay for 400 to 600 units is RS:",charge,"/-")
            else:
                charge = unit * 2.00
                print("Amount to pay for 600 and above units is RS:",charge,"/-")
else:
    print("Enter the Valid Units!!")



print("-------------------------------ELECTRICITY BILL-------------------------------------------")
print("CUSTOMER ID IS :",customer_id)
print("Number of UNITS Consumed By the User are:",unit)
if charge >= 400:
        charge = charge + 15/100
        print("IF THE BILL IS ABOVE 400/- ,Bill will surcharged with 15%\n NEW BILL IS :",charge,"/-")
        print("THE MINIMUM BILL SHOULD BE OF RS 200/- !!!")
else:
    print("BILL paid by Customer is RS:",charge,"/-")
    print("THE MINIMUM BILL SHOULD BE OF RS 200/- !!!")

    
    

