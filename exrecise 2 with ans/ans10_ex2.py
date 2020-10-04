#Question 10: - If five-digit number is entered through keyboard. Write a program to obtained the
#reversed number and to determine whether the original and reversed numbers are equal or not.

num=int (input ("Enter any Five - Digit Number:"))
#%=remainder
#// =round of and remove last digit
temp = num #12389

rem = temp % 10 #9
result = (rem * 10000) #90000

temp = temp // 10 #1238

rem = temp % 10 #8
result = ( result + (  rem * 1000))

temp = temp//10 #123

rem = temp % 10 #3
result = (result + (rem  * 100))

temp = temp //10 #12

rem = temp % 10 #2
result = (result + (rem * 10))

temp = temp // 10 #1

rem = temp % 10
result = ( result + ( rem  * 1))
print("Reversed Number is :",result)
if result==num:
    print("The Reversed Number is Equal to the Original Number")
else:
    print("The Reversed Number is Not Equal to Original Number")
    
