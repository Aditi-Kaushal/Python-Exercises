'''Question 16: - A cashier has currency notes of denomination 10, 50 and 100. If the amount to be
withdrawn is input through the keyboard. Find the total number of currency notes of each
denomination the cashier will have to give the withdrawer.
'''
amount = int(input("Enter the Amount :"))
temp=amount

notes=temp//100

print("Cashier will give 100 Notes as:",notes)
temp=temp%100

notes=temp//50

print("Cashier will give 50 Notes as:",notes)
temp=temp%50

notes=temp//10

print("Cashier will give 10 notes as :",notes)
temp=temp%10




