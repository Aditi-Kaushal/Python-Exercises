#Question 1: - Any year is entered through the keyboard, write a program to determine whether the
#year is leap or not.
year = int ( input ("Enter Any year :"))
if year % 4 == 0:
    print("This Year is a Leap Year")
else:
    print("This is Not a Leap Year")
