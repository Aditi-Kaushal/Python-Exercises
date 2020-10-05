# Input a five digit number and calculate its sum of digits
num = int(input(" Enter Any Five Digit Number: "))

# Let us assume num = 85746
temp = num

rem = temp % 10 # rem = 85746 % 10 = 6 ( Unit Place Digit )

sum = rem # sum = 6

temp = temp // 10 # temp = 85746 // 10 = 8574

rem = temp % 10 # rem = 8574 % 10 = 4 ( Tenth Place Digit )

sum = sum + rem # sum = 6 + 4 = 10

temp = temp // 10 # temp = 8574 // 10 = 857

rem = temp % 10 # rem = 857 % 10 = 7 ( 100th Place Digit )

sum = sum + rem # sum = 10 + 7 = 17

temp = temp // 10 # temp = 857 // 10 = 85 

rem = temp % 10 # rem = 85 % 10 = 5 ( 1000th Place Digit )

sum = sum + rem # sum = 17 + 5 = 22

temp = temp // 10 # temp = 85 // 10 = 8
 
rem = temp % 10 # rem = 8 % 10 = 8 ( 10000th Place Digit )

sum = sum + rem # sum = 22 + 8 = 30

print(" Sum of Digit of Given Number: ",sum)
