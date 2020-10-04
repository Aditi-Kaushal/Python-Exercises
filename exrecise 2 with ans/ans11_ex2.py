'''Question 11: - If the ages of Ram, Shyam and Ajay are input through the keyboard. Write a program
to determine the youngest of the three and display his name.'''
ram= int (input ("Enter the Age of Ram:"))
shyam= int ( input ("Enter the Age of Shyam:"))
ajay= int (input ("Enter the Age of Ajay:"))
if ram < shyam:
    if ram < ajay :
        print("Ram is the Youngest:",ram)
    else:
        print("Ajay is the Youngest:",ajay)
elif shyam < ram:
    if shyam < ajay:
        print("Shyam is the Youngest:",shyam)
    else:
        print("Ajay is Youngest:",ajay)

elif ajay < ram :
    if ajay < shyam :
        print("Ajay is Youngest:",ajay)
    else:
        print("Shyam is the Youngest:",shyam)
else:
    print("Shyam is the Youngest:",shyam)
