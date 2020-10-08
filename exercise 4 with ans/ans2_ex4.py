#Question 2:- Input any Number and find out its sum of digit except first and last digit
num = int (input ("Enter Any Number:")) #12345

temp = num
if temp <0:
    temp = temp * -1

rem= temp % 10
sum = 0

while temp > 0: #12345
    rem2= temp %10
    temp = temp //10
    sum=sum +rem2
sum= sum-rem-temp
print("Sum of Digits of the Given Number Except its First & Last digit is :",sum)



