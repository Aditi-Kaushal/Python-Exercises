#Question 1:- Input any Number and find out its sum of first and last digit.
num= int (input ("Enter Any Number:"))

temp = num#12345
if temp < 0:
    temp = temp * -1

sum= 0
rem = temp % 10 #5
while temp > 1: 
    temp = temp // 10 
    
sum= sum+rem +temp
print("Sum of Firs and Lat digit of the Number is :",sum)
    
