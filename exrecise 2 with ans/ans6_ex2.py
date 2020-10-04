'''Question 6: - If cost price and selling price of an item is input through the keyboard, write a program
to determine whether the seller has made profit or incurred loss. And also determine how much
profit he made or loss he incurred.

'''

cp=int (input ("Enter the Cost Price:"))
sp= int ( input ("Enter The Selling Price"))

if sp>cp:
    Profit = sp-cp
    print("He made Profit as:",Profit)
else:
    Loss = cp - sp
    print("He incurred Loss as :",Loss)
